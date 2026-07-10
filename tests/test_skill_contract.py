from pathlib import Path
import unittest


SKILL = Path(__file__).parents[1] / "plugins" / "submission-package-coach" / "skills" / "submission-package-coach" / "SKILL.md"


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
            "academic-research-suite",
            "deep-paper-reviewer",
            "nature-skills",
        ]

        for phrase in required_phrases:
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
