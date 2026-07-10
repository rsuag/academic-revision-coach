# Product Research Notes

Research date: 2026-07-10

## Signals Used

- [PaperMentor](https://arxiv.org/abs/2606.08857) reports a human-centered workflow that leaves writing to authors and presents actionable comments. This supports an audit-first default.
- [Microsoft Research on AI writing oversight](https://www.microsoft.com/en-us/research/publication/from-use-to-oversight-how-mental-models-influence-user-behavior-and-output-in-ai-writing-assistants/) finds that users' mental models influence how critically they oversee suggestions. This supports explicit boundaries and author confirmation.
- [Nature response skill](https://github.com/Yuan1z0825/nature-skills/blob/main/skills/nature-response/README.md) and [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills) show demand for response-letter and submission-package workflows, but a router should not duplicate their full protocols.
- Public academic-writing discussions repeatedly raise factual drift, invented citations, loss of nuance, verbose output, and the time required to repair generic AI prose. These are directional product signals, not prevalence estimates.

## Product Decisions

| Pain point | First-release response |
| --- | --- |
| The model rewrites too much | `audit only` is the default; drafting needs explicit opt-in. |
| Package-level inconsistencies are missed | A minimal fact ledger and one deduplicated cross-document finding per inconsistency. |
| Users waste tokens pasting everything | Narrow-task loading rules and scenario router. |
| Mentor feedback cannot be reused | Reviewable profiles with evidence count and explicit user-confirmed learning. |
| Generic AI voice | Flag padding and style risks, but never claim to detect AI authorship. |
| Existing workflows overlap | Explicit hand-off to specialist skills, not a copied monolith. |

## Validation Plan

Before expanding features, collect anonymized test cases for: one missed cross-document contradiction, one false-positive style flag, one accepted mentor-rule extraction, and one rejected extraction. Add a regression example for each confirmed failure.
