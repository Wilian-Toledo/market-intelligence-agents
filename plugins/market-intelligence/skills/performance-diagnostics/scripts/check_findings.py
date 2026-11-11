#!/usr/bin/env python3
"""Verifica consistência de achados contra o catálogo local de KPIs (stdlib, sem rede).
Não verifica valores DAX, causalidade nem aprovação de negócio.
Uso: python check_findings.py <achados.json> <catalogo-kpis.json>
"""
import json
import re
import sys
from pathlib import Path

VALID_STATUS = {"approved", "provisional", "restricted", "rejected", "blocked"}
FINDING_TYPES = {"observation", "hypothesis"}
CONFIDENCE = {"preliminary", "validated"}
MODES = {"exploratory", "executive_ready"}


def validate_findings(document, catalog):
    errors = []
    if not isinstance(document, dict) or not isinstance(catalog, dict):
        return ["Documento e catálogo devem ser objetos JSON."]
    if document.get("schema_version") != "0.3":
        errors.append("schema_version deve ser '0.3'.")
    mode = document.get("mode")
    if mode not in MODES:
        errors.append("mode inválido.")
    for field in ("analysis_question", "catalog_path"):
        if not isinstance(document.get(field), str) or not document[field].strip():
            errors.append(f"{field} ausente.")
    if catalog.get("schema_version") != "0.2":
        errors.append("Catálogo KPI precisa usar schema_version '0.2'.")
    indicators = catalog.get("indicators")
    if not isinstance(indicators, list):
        return errors + ["Catálogo sem indicators válido."]
    lookup = {}
    for i in indicators:
        if isinstance(i, dict) and isinstance(i.get("id"), str):
            lookup[i["id"]] = i
    findings = document.get("findings")
    if not isinstance(findings, list) or len(findings) > 5:
        return errors + ["findings deve ser lista com até 5 itens."]
    seen = set()
    for n, finding in enumerate(findings, 1):
        p = f"Achado {n}"
        if not isinstance(finding, dict):
            errors.append(f"{p}: objeto inválido.")
            continue
        fid = finding.get("id")
        if not isinstance(fid, str) or not re.fullmatch(r"[a-zA-Z0-9._-]+", fid):
            errors.append(f"{p}: id inválido.")
        elif fid in seen:
            errors.append(f"{p}: id duplicado.")
        else:
            seen.add(fid)
        for field in ("headline", "period", "segment", "next_check"):
            if not isinstance(finding.get(field), str) or not finding[field].strip():
                errors.append(f"{p}: {field} obrigatório.")
        kind = finding.get("finding_type")
        confidence = finding.get("confidence")
        if kind not in FINDING_TYPES:
            errors.append(f"{p}: finding_type inválido.")
        if confidence not in CONFIDENCE:
            errors.append(f"{p}: confidence inválido.")
        if kind == "hypothesis" and confidence == "validated":
            errors.append(f"{p}: hipótese sem teste causal não pode ser validated.")
        kpis = finding.get("kpi_ids")
        if not isinstance(kpis, list) or not kpis or any(not isinstance(x, str) for x in kpis):
            errors.append(f"{p}: kpi_ids inválido.")
            continue
        if len(set(kpis)) != len(kpis):
            errors.append(f"{p}: IDs de KPI duplicados.")
        for field in ("evidence_refs", "limitations"):
            v = finding.get(field)
            if not isinstance(v, list) or not v or any(not isinstance(x, str) or not x.strip() for x in v):
                errors.append(f"{p}: {field} exige pelo menos uma descrição ou referência.")
        restricted_ok = finding.get("restricted_conditions_verified")
        restricted_evidence = finding.get("restriction_evidence_refs")
        if not isinstance(restricted_ok, bool):
            errors.append(f"{p}: restricted_conditions_verified precisa ser booleano.")
        if not isinstance(restricted_evidence, list) or any(not isinstance(x, str) or not x.strip() for x in restricted_evidence):
            errors.append(f"{p}: restriction_evidence_refs inválido.")
            restricted_evidence = []
        referenced = []
        for kpi_id in kpis:
            kpi = lookup.get(kpi_id)
            if kpi is None:
                errors.append(f"{p}: KPI não encontrado no catálogo: {kpi_id}")
            else:
                referenced.append(kpi)
                status = kpi.get("status")
                if status not in VALID_STATUS or status in {"rejected", "blocked"}:
                    errors.append(f"{p}: KPI {kpi_id} não utilizável ({status}).")
                if "exploratory" not in kpi.get("allowed_uses", []):
                    errors.append(f"{p}: KPI {kpi_id} não liberado para exploração.")
                if status == "restricted" and (restricted_ok is not True or not restricted_evidence):
                    errors.append(f"{p}: KPI {kpi_id} restrito sem checagem e evidência de condições.")
                if mode == "executive_ready" and (status != "approved" or "executive" not in kpi.get("allowed_uses", [])):
                    errors.append(f"{p}: modo executive_ready requer KPIs aprovados.")
        if any(k.get("status") != "approved" for k in referenced) and confidence != "preliminary":
            errors.append(f"{p}: KPI provisório/restrito exige confiança preliminary.")
        if mode == "executive_ready" and confidence != "validated":
            errors.append(f"{p}: modo executivo exige achados validated.")
    if mode == "executive_ready" and not findings:
        errors.append("Não há achados validados para modo executivo.")
    return errors


def main(args):
    if len(args) != 3:
        print("Uso: python check_findings.py <achados-local.json> <catalogo-local.json>", file=sys.stderr)
        return 2
    try:
        doc = json.loads(Path(args[1]).read_text(encoding="utf-8-sig"))
        catalog = json.loads(Path(args[2]).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        print(f"Erro na leitura de arquivo local: {exc}", file=sys.stderr)
        return 2
    errors = validate_findings(doc, catalog)
    if errors:
        for err in errors:
            print("ERRO:", err)
        return 1
    print(f"OK: {len(doc['findings'])} achados consistentes com status de KPI.")
    print("Atenção: não verifica DAX, reconciliação de valores nem causalidade.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
