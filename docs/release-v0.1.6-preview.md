# Task Conductor v0.1.6-preview

This preview removes default fixed Codex cycle budgets and keeps work moving
within existing authorization while preserving evidence-based acceptance.

## Changes

- Workers and reviewers stop on completion, lack of a useful authorized next
  action, missing required input, or an explicit hard limit. They no longer need
  a coordinator-invented model/tool-cycle or correction-count budget.
- Explicit user and repository limits remain binding across follow-ups. External
  executors retain their own retry and remediation policies.
- Existing scoped topology and concurrency authorization is reused across batches.
- Read-only workers do not need synthetic branches, worktrees, or merge gates.
  Commands that mutate caches or outputs still require resource isolation.
- Same-task compaction refreshes durable state and continues; a full transfer
  procedure applies when ownership actually changes.
- The AGY integration reference delegates executor policy to the installed
  delegate-to-agy skill and retains dispatch, handoff, and acceptance requirements.

## Validation and limits

This is an instruction-only release. Validation covers skill structure, local
reference resolution, scoped diff hygiene, and static scenario review for progress,
hard limits, authorization reuse, read-only dispatch, compaction, and AGY handoff.
No new live orchestration pilot or model-performance comparison is claimed.
Existing preview blockers in the release checklist remain open.

## Install

```text
Use $skill-installer to install skills/task-conductor from
mujikawa/codex-task-conductor at ref v0.1.6-preview.
```

For the clarified AGY handoff policy, install the optional delegate-to-agy v0.1.5
release separately. Task Conductor alone does not authorize AGY disclosure.
