import json
from pathlib import Path
import unittest


SKILL = Path(__file__).parents[1] / "plugins" / "submission-package-coach" / "skills" / "submission-package-coach" / "SKILL.md"
ROOT = SKILL.parents[2]


class SkillContractTests(unittest.TestCase):
    def test_safety_and_routing_contracts_are_present(self):
        text = SKILL.read_text(encoding="utf-8")

        required_phrases = [
            "Do not edit any document.",
            "Submission Package Audit",
            "Reviewer Response / Response Letter",
            "Cover Letter",
            "Supporting Information",
            "Manuscript Section",
            "Mentor / Advisor Style Profile",
            "Output Router",
            "project-brief.md",
            "release gate",
            "academic-research-suite",
            "deep-paper-reviewer",
            "nature-skills",
        ]

        for phrase in required_phrases:
            self.assertIn(phrase, text)

    def test_references_and_templates_exist(self):
        required_paths = [
            ROOT / "templates" / "project-brief.md",
            ROOT / "references" / "output-contracts.md",
            ROOT / "references" / "prompt-cards.md",
            ROOT / "references" / "profile-rules.md",
            ROOT / "references" / "release-gate.md",
        ]

        for path in required_paths:
            self.assertTrue(path.is_file(), path)

    def test_regression_cases_are_actionable(self):
        fixtures = json.loads((Path(__file__).parent / "fixtures.json").read_text(encoding="utf-8"))

        self.assertEqual(1, fixtures["schema_version"])
        self.assertGreaterEqual(len(fixtures["cases"]), 4)
        for case in fixtures["cases"]:
            self.assertTrue(case["id"])
            self.assertTrue(case["route"])
            self.assertTrue(case["input"])
            self.assertTrue(case["expected_findings"])
            for finding in case["expected_findings"]:
                self.assertIn(finding["severity"], {"P0", "P1", "P2"})
                self.assertTrue(finding["category"])
                self.assertTrue(finding["evidence"])

    def test_readme_explains_installation_and_routing(self):
        readme = (Path(__file__).parents[1] / "README.md").read_text(encoding="utf-8")

        required_phrases = [
            "## How to Use",
            "codex plugin marketplace add .",
            "codex plugin add submission-package-coach@academic-revision-coach",
            "## Decision Flow",
            "```mermaid",
            "## Similar Skills and the Boundary",
            "What Academic Revision Coach adds",
        ]

        for phrase in required_phrases:
            self.assertIn(phrase, readme)


if __name__ == "__main__":
    unittest.main()
