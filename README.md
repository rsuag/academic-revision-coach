# Academic Revision Coach

An installable Codex plugin for the final, high-stakes stage of academic submission. It routes manuscript, response letter, cover letter, and supporting-information work to compact prompts that preserve author control.

The default is deliberately conservative: it prints a prioritized audit report and minimal manual actions. It does not silently rewrite your files, invent missing evidence, or turn every concern into generic prose.

## Why It Exists

The first release targets recurring problems in AI-assisted academic revision:

- Full-package drift: the manuscript, response letter, cover letter, and SI say slightly different things.
- Loss of author control: a model rewrites instead of identifying the smallest defensible change.
- Context and token waste: users repeatedly paste the entire paper for a narrow response-letter issue.
- Generic, verbose, or recognizably AI-like language.
- Mentor edits are useful but remain trapped in one Word file instead of becoming reusable, reviewable style rules.

The design is informed by public discussions and tools that emphasize human oversight, actionable comments, source fidelity, and package-level traceability. See [Research notes](docs/research-notes.md).

## What It Does

- Routes six scenarios: package audit, reviewer response, cover letter, supporting information, manuscript section, and mentor-style profiling.
- Defaults to `audit only`; drafting and direct editing require explicit user choice.
- Uses a minimal cross-document fact ledger before a package audit, then deduplicates findings by risk.
- Lets users supply an author voice profile and a mentor/advisor profile.
- Learns only through explicit user-approved profile updates.
- Escalates to installed specialist skills instead of reproducing their large workflows.

## Quick Start

Install the `submission-package-coach` plugin from this repository's marketplace, then start a new Codex task and say one of:

```text
Audit my submission package; print findings only.
Create a mentor-style profile from these tracked edits.
Give me a minimal prompt for this reviewer response.
```

The skill asks only for missing information that affects the result. For an audit, identify which copies are authoritative before supplying multiple manuscript versions.

## Profile Workflow

1. Copy `plugins/submission-package-coach/templates/author-style-profile.md` into your manuscript project if you want persistent voice preferences.
2. Supply representative mentor-tracked edits or comments and ask for a profile.
3. Review the extracted rules. Keep one-off edits as examples, not universal policy.
4. After a session, explicitly request a profile update based on accepted or rejected suggestions.

Do not commit confidential manuscripts, reviewer reports, or mentor annotations to this public repository.

## Related Skills

This plugin is intentionally a thin orchestration layer.

- `academic-research-suite`: integrity, citations, re-review, and full response traceability.
- `deep-paper-reviewer`: domain-specific environmental microbiology, microbial ecology, and biogeochemistry review.
- `nature-skills`: Nature-family workflow where journal-specific guidance matters.

## Development

Validate the plugin:

```bash
python3 /Users/ruilinsu/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/submission-package-coach
```

For each release, test the six routes against anonymized examples and record false positives, missed contradictions, and user-accepted suggestions in GitHub Issues. A rule should change only when it has a clear failure case and an explicit expected behavior.

## License

MIT. See [LICENSE](LICENSE).
