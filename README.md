# Academic Revision Coach

An installable Codex plugin for the final, high-stakes stage of academic submission. It routes manuscript, response letter, cover letter, and supporting-information work to compact prompts that preserve author control.

The default is deliberately conservative: it prints a prioritized audit report and minimal manual actions. It does not silently rewrite your files, invent missing evidence, or turn every concern into generic prose.

## Version 0.2

`v0.2.0` adds the pieces that make a prompt workflow dependable across revision rounds:

- `project-brief.md` records the authoritative files, facts, constraints, and open decisions once.
- One output contract per task prevents a request for a prompt from becoming an unsolicited rewrite.
- Prompt cards give copyable, scenario-specific instructions without loading unrelated rules.
- A release gate returns an auditable `READY`, `READY AFTER FIXES`, or `NOT READY` decision.
- Mentor rules have evidence counts, confidence, scope, exceptions, and counterexamples.
- Four anonymized regression cases keep future changes tied to real failure modes.

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
- Uses a reusable project brief and a minimal cross-document fact ledger before a package audit, then deduplicates findings by risk.
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

For work that will recur, first create a `project-brief.md` from `plugins/submission-package-coach/templates/project-brief.md`. This keeps version choices, package scope, and open author decisions visible without pasting the whole project into every task.

## Output Contracts

Choose one output type per request:

- `audit report`: evidence-bound findings and minimal manual actions.
- `prompt card`: one concise prompt to run elsewhere.
- `comment table`: collaborator-ready review comments.
- `draft suggestions`: isolated edits, only after explicit opt-in.
- `release gate`: final package decision with blocking evidence gaps.

The prompt cards and exact schemas live in `plugins/submission-package-coach/references/`; the skill loads only the relevant one.

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

Run the regression contract before changing routes or prompt cards:

```bash
python3 -m unittest discover -s tests -v
```

The initial cases cover number drift, a response claiming an absent edit, SI-label drift, and over-generalizing one mentor edit. Add a sanitized fixture before changing a rule that fixes a new failure. Report regressions or narrow workflow requests through the GitHub issue templates. Never post confidential manuscripts, reviewer reports, data, or mentor annotations.

## License

MIT. See [LICENSE](LICENSE).
