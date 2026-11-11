#!/usr/bin/env python3
"""Checagem local e opcional de contratos de KPI; stdlib, sem rede nem acesso ao PBIX.
Este script NÃO substitui a validação de negócio ou os testes DAX.
Uso: python check_contract.py reports/semantic-validation/01-catalogo-kpis.json
"""
import json
import re
import sys
from pathlib import Path

STATUSES = {"approved", "provisional", "restricted", "rejected", "blocked"}
TECHNICAL = {"verified", "failed", "not_tested"}
BUSINESS = {"confirmed", "pending"}
USES = {"exploratory", "executive"}
TEST_RESULTS = {"passed", "failed", "not_run"}
CHECK_STATES = {"passed", "failed", "unknown"}
YM = re.compile(r"^(\d{4})-(0[1-9]|1[0-2])$")


def month_index(value):
    if not isinstance(value, str):
        return None
    match = YM.fullmatch(value)
    if match is None:
        return None
    return int(match.group(1)) * 12 + int(match.group(2)) - 1


def validate_catalog(data):
    errors = []
    if not isinstance(data, dict):
        return ["Catálogo: raiz deve ser objeto JSON."]
    if data.get("schema_version") != "0.2":
        errors.append("Catálogo: schema_version deve ser '0.2'.")
    for field in ("analysis_question", "model_reference"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"Catálogo: {field} ausente ou vazio.")
    indicators = data.get("indicators")
    if not isinstance(indicators, list):
        return errors + ["Catálogo: indicators deve ser uma lista."]
    seen = set()
    for number, item in enumerate(indicators, 1):
        p = f"Indicador {number}"
        if not isinstance(item, dict):
            errors.append(f"{p}: item precisa ser objeto.")
            continue
        ident = item.get("id")
        if not isinstance(ident, str) or not re.fullmatch(r"[A-Za-z0-9._-]+", ident):
            errors.append(f"{p}: id inválido (use letras, números, ponto, hífen ou _).")
        elif ident in seen:
            errors.append(f"{p}: id duplicado.")
        else:
            seen.add(ident)
        if not isinstance(item.get("name"), str) or not item["name"].strip():
            errors.append(f"{p}: name ausente.")
        status = item.get("status")
        tech = item.get("technical_validation")
        business = item.get("business_validation")
        if status not in STATUSES:
            errors.append(f"{p}: status inválido.")
        if tech not in TECHNICAL:
            errors.append(f"{p}: technical_validation inválido.")
        if business not in BUSINESS:
            errors.append(f"{p}: business_validation inválido.")
        if not isinstance(item.get("unit"), str) or not item["unit"].strip():
            errors.append(f"{p}: unit ausente.")
        scope = item.get("scope")
        if not isinstance(scope, dict) or any(
            not isinstance(scope.get(key), str) or not scope[key].strip()
            for key in ("granularity", "period", "population")
        ) or not isinstance(scope.get("filters"), list):
            errors.append(f"{p}: scope incompleto.")
        lineage = item.get("lineage")
        if not isinstance(lineage, list) or not lineage or any(
            not isinstance(x, str) or not x.strip() for x in lineage
        ):
            errors.append(f"{p}: lineage deve conter fontes/evidências locais.")
        evidence = item.get("evidence")
        if not isinstance(evidence, list):
            errors.append(f"{p}: evidence deve ser lista.")
            evidence = []
        for e in evidence:
            if not isinstance(e, dict) or not e.get("test") or not e.get("reference") or e.get("result") not in TEST_RESULTS:
                errors.append(f"{p}: registro de evidência incompleto.")
        passed = any(isinstance(e, dict) and e.get("result") == "passed" for e in evidence)
        failed = any(isinstance(e, dict) and e.get("result") == "failed" for e in evidence)
        restrictions = item.get("restrictions")
        blockers = item.get("blockers")
        uses = item.get("allowed_uses")
        if not isinstance(restrictions, list):
            errors.append(f"{p}: restrictions deve ser lista.")
            restrictions = []
        if not isinstance(blockers, list):
            errors.append(f"{p}: blockers deve ser lista.")
            blockers = []
        if not isinstance(uses, list) or any(not isinstance(u, str) or u not in USES for u in uses) or len(uses) != len(set(uses)):
            errors.append(f"{p}: allowed_uses inválido.")
            uses = []
        expected = {
            "approved": {"exploratory", "executive"},
            "provisional": {"exploratory"},
            "restricted": {"exploratory"},
            "rejected": set(),
            "blocked": set(),
        }.get(status)
        if expected is not None and set(uses) != expected:
            errors.append(f"{p}: allowed_uses incompatível com status {status}.")
        if tech == "failed" and status != "rejected":
            errors.append(f"{p}: teste técnico falho exige status rejected.")
        if failed and status != "rejected":
            errors.append(f"{p}: evidência reprovada exige status rejected.")
        if status == "approved" and (tech != "verified" or business != "confirmed" or not passed):
            errors.append(f"{p}: approved exige verificação técnica, negócio confirmado e teste aprovado.")
        if status in {"provisional", "restricted"} and (tech != "verified" or not passed):
            errors.append(f"{p}: {status} exige verificação técnica e teste aprovado.")
        if status == "restricted" and not restrictions:
            errors.append(f"{p}: restricted exige restrições documentadas.")
        if status == "blocked" and not blockers:
            errors.append(f"{p}: blocked exige motivo de bloqueio.")
        if status == "rejected" and tech != "failed" and not failed:
            errors.append(f"{p}: rejected exige evidência explícita de falha.")
        if status in {"approved", "provisional", "restricted"} and blockers:
            errors.append(f"{p}: indicador utilizável não pode conter bloqueios críticos.")
        comparison = item.get("comparison")
        if comparison is not None:
            if not isinstance(comparison, dict) or comparison.get("kind") not in {"none", "yoy", "sequential"}:
                errors.append(f"{p}: comparison.kind inválido.")
            elif comparison["kind"] != "none":
                dates = [month_index(comparison.get(k)) for k in (
                    "current_start", "current_end", "reference_start", "reference_end"
                )]
                if any(x is None for x in dates):
                    errors.append(f"{p}: períodos devem ser YYYY-MM.")
                else:
                    cs, ce, rs, re_ = dates
                    if ce < cs or re_ < rs or (ce - cs) != (re_ - rs):
                        errors.append(f"{p}: janelas comparadas têm durações diferentes ou inversão.") if status != "rejected" else None
                    elif comparison["kind"] == "yoy" and (cs-rs != 12 or ce-re_ != 12):
                        errors.append(f"{p}: yoy exige mesma janela deslocada exatamente 12 meses.") if status != "rejected" else None
                    elif comparison["kind"] == "sequential" and re_ != cs-1:
                        errors.append(f"{p}: sequential exige janela imediatamente anterior.") if status != "rejected" else None
        ratio = item.get("ratio_checks")
        if ratio is not None:
            keys = ("period_alignment", "unit_alignment", "population_alignment", "filter_isolation")
            if not isinstance(ratio, dict) or any(ratio.get(k) not in CHECK_STATES for k in keys):
                errors.append(f"{p}: ratio_checks incompleto.")
            elif any(ratio[k] == "failed" for k in keys) and status != "rejected":
                errors.append(f"{p}: razão com checagem reprovada exige status rejected.")
            elif status == "approved" and any(ratio[k] != "passed" for k in keys):
                errors.append(f"{p}: razão com alinhamento não confirmado não pode ser approved.")
    return errors


def main(argv):
    if len(argv) != 2:
        print("Uso: python check_contract.py <catalogo-local.json>", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(argv[1]).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        print(f"Falha ao ler catálogo local: {exc}", file=sys.stderr)
        return 2
    errors = validate_catalog(data)
    if errors:
        for err in errors:
            print("ERRO:", err)
        return 1
    print(f"OK: {len(data['indicators'])} contratos passaram nas checagens estruturais e de consistência.")
    print("Atenção: NÃO comprova correção DAX, reconciliação com a origem ou validação de negócio.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
