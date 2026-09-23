# Task Conductor v0.1.9-preview

Workers and reviewers previously inherited their creator's model and effort
unless the user selected an override. Authorized workers now default to
`gpt-6-sol` / `high`, and independent reviewers, when needed, to
`gpt-6-sol` / `xhigh`. Coordinators retain their current settings.

Explicit user choices override user-adopted project role settings, then skill
defaults. Profiles must be supported by the host and passed through creation
fields. The workflow records selected settings and their sources, with actual
settings when observable; it does not silently substitute unsupported profiles.

Codex direct remains the executor default. An explicit user request can enable
one worker-owned Luna executor, defaulting to `gpt-6-luna` / `xhigh`. It holds the
outcome's exclusive write ownership while running, cannot delegate further, and
returns actual changes and checks for the owning worker to verify. The worker
retains outcome accountability and may resume implementation only after a verified
handoff within authorized scope. AGY remains explicitly opt-in under its existing
separately installed delegation skill.

These settings do not automatically create a reviewer, enable nested agents,
increase concurrency, switch executors or escalate reasoning effort. Same-outcome
follow-ups preserve the resolved profile. Existing progress-based execution,
single broad-gate ownership and optional version-1 receipts remain in place.

## Install

```text
Use $skill-installer to install skills/task-conductor from
mujikawa/codex-task-conductor at ref v0.1.9-preview.
```

## Validation and status

Release gates cover the existing offline receipt tests, official skill validation,
local Markdown links, diff hygiene, exact-source installation comparison and a
fresh-process recognition smoke test. Record actual results in the release/PR
evidence. Recognition is not a live nested-executor delivery pilot.

This remains a preview. The role defaults are quality-oriented starting policies;
their effect on accepted-outcome cost, latency, rework and escaped defects has not
been benchmarked. A live Luna executor pilot remains outstanding.
