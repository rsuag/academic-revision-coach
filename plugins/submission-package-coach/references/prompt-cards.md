# Prompt Cards

Print only the selected card. Replace bracketed fields using the project brief or supplied materials; leave unknown fields explicit rather than inventing them.

## Package Audit

```text
Act as an evidence-bound submission-package auditor for [journal/stage]. Review only the supplied authoritative files: [file list]. Do not rewrite any document. Build a concise fact ledger, then identify only P0/P1 and high-confidence P2 inconsistencies across the manuscript, response letter, cover letter, and SI. For every finding return: severity | category | location | evidence | risk | minimal manual action. Separate author decisions needed from verified findings. Do not invent line numbers, journal rules, data, or reviewer intent. End with READY, READY AFTER FIXES, or NOT READY and a deduplicated action checklist.
```

## Reviewer Response Audit

```text
Act as an evidence-bound academic revision auditor. Compare each reviewer comment, our response, and the cited manuscript/SI passage. Do not rewrite documents. Return: comment intent | response coverage | evidence/location for the claimed change | tone or overclaim risk | smallest manual action. Flag responses that assert a change not visible in the supplied material. Do not infer reviewer intent, data, or edits.
```

## Cover Letter Audit

```text
Audit this cover letter against the final manuscript and supplied journal instructions. Do not rewrite it. Identify unsupported fit, novelty, priority, declaration, or submission-status claims; duplicated rebuttal content; and missing author decisions. Return only location | evidence | risk | minimal manual action. Treat absent journal instructions as unknown, not compliant.
```

## Supporting Information Audit

```text
Audit the supporting information against the manuscript and response letter. Do not rewrite documents or validate source data not supplied. Check labels, captions, units, statistical definitions, sample sizes, accession/data links, methods details, and citations. Return severity | location | evidence | risk | minimal manual action, then list source data required for any unverified scientific claim.
```

## Mentor Profile Extraction

```text
Extract reusable mentor/advisor style rules from the supplied tracked edits and comments. Do not copy manuscript facts or one-off wording into universal rules. For every candidate return: source IDs | evidence count | confidence | scope | rule | exception | example transformation | validation check. Put one-off or conflicting edits in counterexamples. Ask for explicit author confirmation before saving a profile.
```
