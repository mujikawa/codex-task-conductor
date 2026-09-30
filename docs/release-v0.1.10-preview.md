# Task Conductor v0.1.10-preview

New authorized workers now default to `gpt-6.1-sol` / `high`, and independent
reviewers, when needed, to `gpt-6.1-sol` / `xhigh`. This replaces the GPT-6 Sol
defaults introduced in v0.1.9-preview.

Coordinators retain their current settings. Explicit user choices and adopted
project role settings still override skill defaults, and same-outcome follow-ups
preserve an existing agent's resolved profile unless an authorized change applies.
The opt-in Luna executor remains `gpt-6-luna` / `xhigh`; AGY remains governed by
its separately installed skill. Dispatch, acceptance and concurrency rules are
unchanged.

The [official GPT-6.1 Sol model documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
supports the retained reasoning levels. Dispatch must still verify the destination
host supports the selected profile; unsupported settings are never silently
substituted. This release makes no measured quality, latency or cost claim.

## Install

```text
Use $skill-installer to install skills/task-conductor from
mujikawa/codex-task-conductor at ref v0.1.10-preview.
```

## Validation and status

Release gates cover offline receipt regression tests, official skill validation,
local Markdown links, diff hygiene, exact-tag installation comparison and a
fresh-process recognition smoke test. Actual results are recorded in the PR and
published release. Recognition does not establish live delivery performance.

This remains a preview; existing operational limitations and outstanding pilots
remain applicable.
