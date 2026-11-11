#!/usr/bin/env python3
"""Validação estática do toolkit; não lê o modelo nem usa rede."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
assert market["name"] == "market-intelligence-marketplace"
assert market["plugins"], "Marketplace vazio"
for item in market["plugins"]:
    p = (ROOT / item["source"]).resolve()
    assert p.is_relative_to(ROOT.resolve()) and p.is_dir(), str(p)
    meta = json.loads((p / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    assert meta["name"] == item["name"]
    assert meta["version"] == "0.3.0", "Versão do plugin desatualizada"
    agents = list((p / "agents").glob("*.md"))
    skills = list((p / "skills").glob("*/SKILL.md"))
    assert len(agents) >= 2, "Esperados Model Cartographer e Market Diagnostician"
    assert skills, "Nenhuma skill"
    for file in agents + skills:
        assert file.read_text(encoding="utf-8").startswith("---"), file
    assert not (p / ".mcp.json").exists(), "MCP não deve ser incluído"
    for skill_name in ("mapear-modelo", "powerbi-semantic-audit", "semantic-validator", "validar-indicadores", "diagnosticar-desempenho", "performance-diagnostics"):
        assert (p / "skills" / skill_name / "SKILL.md").exists(), skill_name
    validator = p / "skills/semantic-validator"
    assert (validator / "references/kpi-contract.schema.json").exists()
    assert (validator / "scripts/check_contract.py").exists()
    assert (validator / "examples/synthetic-catalog.json").exists()
    diagnostician = p / "skills/performance-diagnostics"
    assert (diagnostician / "references/findings.schema.json").exists()
    assert (diagnostician / "scripts/check_findings.py").exists()
    assert (diagnostician / "examples/synthetic-findings.json").exists()
    json.loads((diagnostician / "references/findings.schema.json").read_text(encoding="utf-8"))
    assert json.loads((diagnostician / "examples/synthetic-findings.json").read_text(encoding="utf-8"))["schema_version"] == "0.3"
    json.loads((validator / "references/kpi-contract.schema.json").read_text(encoding="utf-8"))
    assert json.loads((validator / "examples/synthetic-catalog.json").read_text(encoding="utf-8"))["schema_version"] == "0.2"
json.loads((ROOT / "contracts/audit-summary.schema.json").read_text(encoding="utf-8"))
assert (ROOT / "scripts/install-native.ps1").exists()
print("OK: versão 0.3, marketplace, 2 agentes, 6 skills, contratos e exemplos sintéticos.")
