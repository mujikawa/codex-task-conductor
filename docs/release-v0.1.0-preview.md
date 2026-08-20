# Task Conductor v0.1.0-preview

This preview release changes the default orchestration direction from independent
sidebar tasks to coordinator-owned Codex subagents for bounded automation. It
keeps independent user-owned tasks for lifecycle boundaries and adds an optional
AGY implementation executor without bundling AGY's wrapper or policy.

## Why this changed

Observed workflows showed that `spawn_agent` is easier for a coordinator to
automate because it directly owns dispatch, bounded waits, follow-up, interruption,
and result collection. Independent sidebar tasks remain valuable, but destination
resolution, asynchronous task-ID correlation, saved-project inventory, and
user-owned lifecycle management make them heavier than necessary for ordinary
outcome-level work.

Long-running coordinators also need a durable continuation strategy. The release
therefore adds a context-rollover protocol that checkpoints authoritative state
before compaction or coordinator replacement and prevents duplicate dispatch.

AGY is modeled as an implementation executor rather than a third Codex topology.
A Codex worker can manage `$delegate-to-agy`, independently inspect its changes,
run verification, and return evidence while Task Conductor retains ownership and
acceptance responsibility.

## Installation

Ask Codex:

```text
Use $skill-installer to install skills/task-conductor from
mujikawa/codex-task-conductor at ref v0.1.0-preview.
```

Restart or reload Codex after installation. Then open a fresh task and ask it to
list the active `task-conductor` skill without dispatching work.

`$delegate-to-agy` is optional and must be installed and maintained separately.
Task Conductor does not copy its wrapper, execution policy, authentication, or
runtime configuration.

## Recommended usage

### One coordinator-owned worker

```text
Use $task-conductor for one bounded serial outcome.

Durable tracker: [GitHub Issue or repository-approved tracker]
Outcome: [one independently verifiable result]
Authorized topology: exactly one coordinator-owned subagent
Implementation executor: Codex direct
Required verification: [commands]

Do not create independent tasks, nested subagents, a second worker, a PR,
deployment, or cleanup. Return an immutable candidate for evidence-based
acceptance.
```

### Codex worker with AGY implementation

```text
Use $task-conductor and $delegate-to-agy for one bounded serial outcome.

Durable tracker: [tracker]
Outcome: [one independently verifiable result]
Authorized topology: exactly one coordinator-owned Codex worker subagent
Implementation executor: AGY via $delegate-to-agy
Allowed paths: [exact paths]
Required verification: [commands]
AGY remediation limit: at most two passes

Use a clean linked worktree with one write-capable owner. Keep the AGY
conversation ID in private routing state. Do not create independent tasks,
commits, pushes, deployments, or nested Codex subagents.
```

The Codex worker must review the actual AGY diff and run verification. AGY's
`SUCCESS` status and summary are execution evidence, not acceptance evidence.

### When to use an independent task

Choose an independent user-owned Codex task only when direct user follow-up,
separate authorization or risk, long-lived ownership, a distinct host or
repository, or explicit user preference makes its independent lifecycle useful.
Sidebar placement alone does not prove that a thread is user-owned; verify its
creation operation and lineage.

## Preview limitations

- The subagent-first direction has not completed a clean-room delivery pilot.
- The Task Conductor plus AGY executor contract has not completed a clean-room
  delivery pilot.
- Controlled two-worker parallel mutation has not been validated.
- Recorded token and elapsed-time observations are operational baselines, not
  proof that orchestration reduces cost.

Use the preview for controlled adoption and measurement. Do not describe these
pending capabilities as stable or validated.
