"""Testes sintéticos do gate entre diagnóstico e contrato de KPI."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "plugins/market-intelligence/skills/performance-diagnostics/scripts/check_findings.py"
EXAMPLE = ROOT / "plugins/market-intelligence/skills/performance-diagnostics/examples/synthetic-findings.json"
CATALOG = ROOT / "plugins/market-intelligence/skills/semantic-validator/examples/synthetic-catalog.json"
spec = importlib.util.spec_from_file_location("check_findings", SRC)
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class DiagnosticContractTest(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        self.catalog = json.loads(CATALOG.read_text(encoding="utf-8"))

    def test_synthetic_example_passes(self):
        self.assertEqual(check.validate_findings(self.doc, self.catalog), [])

    def test_rejected_kpi_is_not_usable(self):
        doc = copy.deepcopy(self.doc)
        doc["findings"][0]["kpi_ids"] = ["metric-share-bad"]
        self.assertTrue(any("não utilizável" in e for e in check.validate_findings(doc, self.catalog)))

    def test_provisional_kpi_cannot_justify_executive(self):
        doc = copy.deepcopy(self.doc)
        doc["mode"] = "executive_ready"
        self.assertTrue(any("modo executive_ready" in e for e in check.validate_findings(doc, self.catalog)))

    def test_provisional_finding_not_validated(self):
        doc = copy.deepcopy(self.doc)
        doc["findings"][0]["confidence"] = "validated"
        self.assertTrue(any("preliminary" in e for e in check.validate_findings(doc, self.catalog)))

    def test_unknown_kpi_fails(self):
        doc = copy.deepcopy(self.doc)
        doc["findings"][0]["kpi_ids"] = ["missing-kpi"]
        self.assertTrue(any("não encontrado" in e for e in check.validate_findings(doc, self.catalog)))

    def test_restricted_kpi_requires_evidence(self):
        doc = copy.deepcopy(self.doc)
        catalog = copy.deepcopy(self.catalog)
        catalog["indicators"][0]["status"] = "restricted"
        catalog["indicators"][0]["restrictions"] = ["Somente recorte A"]
        self.assertTrue(any("restrito sem checagem" in e for e in check.validate_findings(doc, catalog)))

    def test_restricted_kpi_with_evidence(self):
        doc = copy.deepcopy(self.doc)
        catalog = copy.deepcopy(self.catalog)
        catalog["indicators"][0]["status"] = "restricted"
        catalog["indicators"][0]["restrictions"] = ["Somente recorte A"]
        doc["findings"][0]["restricted_conditions_verified"] = True
        doc["findings"][0]["restriction_evidence_refs"] = ["exemplo-local/recorte-A"]
        self.assertEqual(check.validate_findings(doc, catalog), [])


if __name__ == "__main__":
    unittest.main()
