# Task Conductor v0.1.2-preview

This preview turns two anonymized Task Conductor plus AGY delivery observations
into cost-aware delegation, capability-handoff, context-loading, and measurement
controls.

## What changed

- An AGY loop budget now separates an economics-based hard cap from a convergence
  checkpoint. A user may select a higher cap such as 10 for a lower-cost executor;
  the workflow stops early when evidence no longer improves.
- AGY may hand off to Codex before the cap when the remaining operation is outside
  its capabilities or permitted tools. The handoff preserves baseline, diff,
  completed criteria, remaining gap, validation, receipt, and one next action.
- Successful AGY receipts remain private and available until the immutable
  candidate and frozen gate pass, enabling later receipt-bound remediation.
- Dispatch packets now declare runtime-artifact ownership and avoid full-history
  inheritance except for the smallest trusted authorization context required.
- AGY receipt telemetry is measured with per-invocation `usage_delta`; cumulative
  same-conversation counters are not counted again on every remediation.
- A new public field observation records the implementation lessons without task,
  conversation, repository, issue, account, or absolute-path identifiers.

## Installation

Ask Codex:

```text
Use $skill-installer to install skills/task-conductor from
mujikawa/codex-task-conductor at ref v0.1.2-preview.
```

Restart or reload Codex after installation. `$delegate-to-agy` remains a separate
optional dependency and must be installed from its own release.

## Preview limitations

- The observations are not controlled cost or efficiency benchmarks. AGY and
  Codex usage remain separate unless token definitions and prices are normalized.
- A formal task omitted from bounded recent-task inventory has not yet been
  reproduced in a fresh case.
- Capability handoff and per-loop receipt telemetry have deterministic wrapper
  tests, but still require further diverse production-shaped pilots.

Use this release for controlled adoption. Worker topology, AGY disclosure, GitHub
publication, deployment, credentials, cleanup, and other external side effects
remain behind their explicit authorization boundaries.
