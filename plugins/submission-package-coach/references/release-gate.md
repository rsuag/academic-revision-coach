# Submission Release Gate

Use this only for the final declared package. Verify the project brief first.

## Decision Rules

- `NOT READY`: any P0 issue, an unresolved P1 issue, an unknown authoritative version for a required package file, or a submission claim without supplied evidence.
- `READY AFTER FIXES`: no P0 issue, but one or more P1/P2 actions remain.
- `READY`: all required files in the brief are authoritative, no P0/P1 issue remains, and all listed blocking decisions are resolved.

## Required Output

```text
Release decision: READY | READY AFTER FIXES | NOT READY
Scope: [authoritative files checked; files not checked]
Blocking evidence gaps: [none or list]
P0/P1 findings: [none or severity | location | evidence | owner]
Open author decisions: [none or ID | decision | release impact]
Required actions before submission: [ordered list]
Residual non-blocking risks: [ordered list]
```

`READY` is a decision about the supplied package only. It is not a guarantee of scientific validity, journal acceptance, or compliance with instructions that were not supplied.
