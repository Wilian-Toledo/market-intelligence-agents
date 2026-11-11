#!/usr/bin/env python3
"""Testes com dados 100% sintéticos. Executar: python -m unittest discover -s tests"""
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "plugins/market-intelligence/skills/semantic-validator/scripts/check_contract.py"
EXAMPLE = ROOT / "plugins/market-intelligence/skills/semantic-validator/examples/synthetic-catalog.json"
spec = importlib.util.spec_from_file_location("check_contract", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ContractValidationTest(unittest.TestCase):
    def setUp(self):
        self.sample = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def test_synthetic_example_is_consistent(self):
        self.assertEqual(module.validate_catalog(self.sample), [])

    def test_yoy_mismatched_period_fails(self):
        obj = copy.deepcopy(self.sample)
        obj["indicators"][0]["comparison"]["reference_start"] = "2025-01"
        self.assertTrue(any("janelas" in e for e in module.validate_catalog(obj)))

    def test_yoy_wrong_year_fails(self):
        obj = copy.deepcopy(self.sample)
        obj["indicators"][0]["comparison"]["reference_start"] = "2024-04"
        obj["indicators"][0]["comparison"]["reference_end"] = "2024-06"
        self.assertTrue(any("yoy" in e for e in module.validate_catalog(obj)))

    def test_unconfirmed_business_cannot_be_approved(self):
        obj = copy.deepcopy(self.sample)
        obj["indicators"][0]["status"] = "approved"
        obj["indicators"][0]["allowed_uses"] = ["exploratory", "executive"]
        self.assertTrue(any("approved" in e for e in module.validate_catalog(obj)))

    def test_failed_evidence_cannot_be_provisional(self):
        obj = copy.deepcopy(self.sample)
        obj["indicators"][0]["evidence"][0]["result"] = "failed"
        self.assertTrue(any("rejected" in e for e in module.validate_catalog(obj)))

    def test_rejected_cannot_be_used(self):
        obj = copy.deepcopy(self.sample)
        obj["indicators"][1]["allowed_uses"] = ["executive"]
        self.assertTrue(any("allowed_uses" in e for e in module.validate_catalog(obj)))

    def test_sequential_valid_windows(self):
        obj = copy.deepcopy(self.sample)
        obj["indicators"][0]["comparison"].update({
            "kind": "sequential", "reference_start": "2026-01", "reference_end": "2026-03"
        })
        self.assertEqual(module.validate_catalog(obj), [])


if __name__ == "__main__":
    unittest.main()
