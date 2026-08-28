# Task prompt templates

Replace bracketed fields and remove fields that do not apply. Propagate the user's requested output language; otherwise preserve the coordinator conversation language.

## Contents

- Worker creation metadata
- Coordinator
- Worker
- Reviewer
- Parallel pilot
- Follow-up
- Ops outcome

## Worker creation metadata

```text
Title: [project/module] | [bounded outcome] | [Coordinator|Worker|Reviewer|Follow-up|Ops]
Topology: [coordinator-owned subagent | independent user-owned task]
Implementation executor: [Codex direct | AGY via $delegate-to-agy]
Execution profile: [default/inherited | model=[user-requested model], reasoning effort=[level], rationale=[why]]
```

Pass title, model, and reasoning effort through creation fields when supported. Omit model and reasoning parameters for configured defaults. Record the returned agent path or task ID.

## Coordinator

```text
Use $task-conductor to coordinate [initiative].

Durable tracker: [tracker]
Target outcome: [initiative outcome]
Authorized topology: [coordinator-owned subagent | independent user-owned task]
Authorized concurrency: [one worker | exact concurrency]
Implementation executor: [Codex direct | AGY via $delegate-to-agy]
Language: [requested language or inherit]
Constraints: [authorization and repository rules]
Initial next action: [one action]

Prefer coordinator-owned subagents unless a separate user-owned lifecycle is material or explicitly requested. Do not implement worker scope or create nested tasks without explicit authorization.
```

## Worker

```text
Deliver exactly this bounded outcome: [outcome].

Durable tracker: [tracker]
Dependencies satisfied: [facts]
In scope: [items]
Out of scope: [items]
Definition of Done: [criteria]
Required validation: [commands and evidence]
Branch/worktree: Use the dedicated task branch and worktree from [pinned base].
Runtime ownership: [environment, cache, port, database, generated-output paths and permitted lifecycle actions]
Authorization boundaries: [boundaries]
Language: [requested language or inherit]

Read current durable state and repository instructions before editing. Do not create nested subagents or tasks. Return the worker completion contract.
```

Build this prompt from the compact dispatch packet in `context-loading.md`. Add:

```text
Model/tool cycle budget: [phase budgets or observable-loop proxy]
Correction envelope: [exact mutable scope, allowed correction loops, focused checks, broad-gate allowance]
Stop conditions: [budget boundary, failed gate, authorization boundary]
Evidence locations: [exact durable references; do not embed raw history]
Frozen candidate gate: [exact repository-wide commands required before review and acceptance]
```

When the executor is AGY, add the compact AGY delegation packet from
`delegate-to-agy.md`. Explicitly instruct the Codex worker to invoke
`$delegate-to-agy`, review the resulting diff independently, and return Codex's
verification rather than AGY's claims.

Add these fields when an AGY loop budget is authorized:

```text
AGY economic hard cap: [maximum loops and cost rationale]
Convergence checkpoint: [new finding, changed diff, or verification progress required after each loop]
Early-stop conditions: [repeated no-progress failure, unsupported operation, deterministic failure, scope or authority boundary]
Runtime artifacts: [environment, dependencies, caches, generated outputs, receipt retention, and authorized cleanup envelope]
Capability handoff: [baseline, actual diff, completed criteria, remaining gap, unavailable operation, evidence, and next Codex action]
```

The hard cap is not a target. Preserve a user-selected higher cap when its economic
rationale is explicit, while stopping early on the declared evidence conditions.

## Reviewer

```text
Review only [outcome] at [repository, branch, HEAD, or review target].

Definition of Done: [criteria]
Required checks: [checks]
Known risks: [risks]
Language: [requested language or inherit]

Do not implement fixes or broaden scope. Return evidence and an accept or needs_followup recommendation.
```

Start a reviewer only after the review readiness gate passes. Populate its prompt
from the compact acceptance packet; do not attach worker chat, full Issue history,
or raw logs when stable evidence locations are available.

## Parallel pilot

```text
Use $task-conductor for a controlled parallel pilot.

Durable trackers: [trackers]
Authorized concurrency: Exactly [2] mutating workers; no nested tasks.
Outcome A: [scope, DoD, branch/worktree, resources, execution profile]
Outcome B: [scope, DoD, branch/worktree, resources, execution profile]
Pinned base and frozen contract: [refs]
Integration order and gate: [order and commands]

Complete every parallel-readiness check before dispatch. If one fails, report the safe serial next action. Accept workers individually, then run integration acceptance.
```

## Follow-up

```text
Continue the same bounded outcome.
Acceptance failed because: [evidence gap].
Required correction: [correction].
Execution profile: [preserve current | user-requested override and rationale]

Do not change scope or Definition of Done. Return updated HEAD, validation, telemetry availability, and durable handoff evidence.
```

## Ops outcome

Use only after delivery acceptance and explicit authorization. Select a
coordinator-owned subagent for bounded automation or an independent task when its
user-owned lifecycle is material:

```text
Operate on the accepted delivery at [immutable target].

Authorized operation: [publish | merge | deploy | migrate | monitor]
Exact side effects: [push | PR creation | merge | reconciliation | deployment | cleanup; remove unauthorized items]
Durable tracker: [tracker and accepted delivery record]
Environment and rollback boundary: [facts]
Rehearsal evidence: [same-platform syntax, fixture, topology, or dry-run evidence required before live mutation]
Required checks and evidence: [checks and stable locations]
Model/tool cycle budget: [budget or observable-loop proxy]
Stop conditions: [failed preflight, drift, budget, or authorization boundary]
Language: [requested language or inherit]

Do not change accepted delivery scope. Return the completion contract and keep this
operation outside the delivery-acceptance measurement boundary.
```

For production cutovers, make health gates enumerate every required dependency and
test platform-dependent assertions against representative output before mutation.
Do not use production retries as the primary parser, quoting, or assertion test
harness.
