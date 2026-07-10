# Output Contracts

Select exactly one unless the author explicitly requests more.

## Audit Report

Use for diagnosis without rewriting. Return: scope checked, prioritized findings, author decisions needed, and minimal action checklist. Each finding must use `severity | category | location | evidence | risk | minimal manual action`.

## Prompt Card

Use when the author wants a prompt to run in another model or a new task. Return one copyable prompt plus at most three required inputs. Do not append an audit or a rewrite.

## Comment Table

Use for Word/Overleaf/collaborator handoff. Return `location | issue | evidence | suggested manual action | author decision`. Do not state a decision as settled when evidence is missing.

## Draft Suggestions

Use only after explicit opt-in. Return isolated candidate edits labelled `suggestion`, each with source location and a one-sentence rationale. Do not rewrite adjacent text or alter facts.

## Release Gate

Use only for a declared final package and read `release-gate.md`. Return the gate schema exactly; never fill missing evidence with optimistic assumptions.
