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
    agents = list((p / "agents").glob("*.md"))
    skills = list((p / "skills").glob("*/SKILL.md"))
    assert agents, "Nenhum agente"
    assert skills, "Nenhuma skill"
    for file in agents + skills:
        assert file.read_text(encoding="utf-8").startswith("---"), file
    assert not (p / ".mcp.json").exists(), "MCP não deve ser incluído"
json.loads((ROOT / "contracts/audit-summary.schema.json").read_text(encoding="utf-8"))
assert (ROOT / "scripts/install-native.ps1").exists()
print("OK: marketplace, plugin, agentes, skills, contrato e instalador.")
