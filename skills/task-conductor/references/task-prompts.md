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
Title: [project/module] | [bounded outcome] | [Coordinator|Worker|Reviewer|Executor|Follow-up|Ops]
Topology: [coordinator-owned subagent | independent user-owned task | explicitly authorized worker-owned Luna subagent]
Implementation executor: [Codex direct (default) | explicitly enabled Luna subagent | explicitly requested AGY via $delegate-to-agy]
Execution profile: [resolved model and effort from SKILL.md role defaults or overrides; default/inherited only when selected]
Profile source: [user choice | user-adopted project role setting | skill role default; record per setting]
```

Resolve profiles using the role table and precedence in `../SKILL.md`. Pass title,
model, and reasoning effort through supported creation fields. Omit model and
effort only when configured defaults/inheritance were selected. Verify host
selection rules and support before dispatch; record the returned agent path or
task ID and actual settings when observable. Do not silently fall back.

## Coordinator

```text
Use $task-conductor to coordinate [initiative].

Durable tracker: [tracker]
Target outcome: [initiative outcome]
Authorized topology: [coordinator-owned subagent | independent user-owned task]
Authorized concurrency limit: [existing authorization and maximum workers]
Implementation executor: [Codex direct (default) | explicitly enabled Luna subagent | explicitly requested AGY via $delegate-to-agy]
Role profile overrides: [user/project choices; omit when using SKILL.md role defaults]
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
Target: [repository and pinned base; dedicated branch/worktree for mutating work]
Runtime ownership: [environment, cache, port, database, generated-output paths and permitted lifecycle actions]
Authorization boundaries: [boundaries]
Authorization anchor: [trusted user turn or standing-policy boundary]
Inherited context: [none | smallest recent slice containing trusted authorization | evidenced full-history exception]
Language: [requested language or inherit]

Read current durable state and repository instructions before editing. Do not create nested subagents or tasks except the explicitly enabled Luna executor described in the attached packet. Return the worker completion contract.
```

Build this prompt from the compact dispatch packet in `context-loading.md`. Add:

```text
Explicit hard limits: [user/repository limits; omit if none]
Correction scope: [already authorized files/components, focused checks, broad-gate owner]
Stop conditions: [completion, no useful authorized next action, missing required input, authority or explicit hard-limit boundary]
Evidence locations: [exact durable references; do not embed raw history]
Validation ownership: [worker semantic/focused checks | immutable-candidate broad gate owner | integration gate owner]
Frozen candidate gate: [exact repository-wide commands required before review and acceptance]
```

When the user enables Luna, add the compact executor packet from
`luna-executor.md`. Explicitly authorize one worker-owned executor layer within
the existing concurrency limit. The worker independently reviews actual changes
and owns the completion record; Luna must not create further agents. Do not add
this layer for ordinary Codex direct work.

When the executor is AGY, add the compact AGY delegation packet from
`delegate-to-agy.md`. Explicitly instruct the Codex worker to invoke
`$delegate-to-agy`, review the resulting diff independently, and return Codex's
verification rather than AGY's claims.

Add these fields when an AGY loop budget is authorized:

```text
AGY economic hard cap: [maximum loops and cost rationale]
External disclosure authorization: [trusted user turn plus exact private paths or content classes]
Convergence checkpoint: [new finding, changed diff, or verification progress required after each loop]
Early-stop conditions: [repeated no-progress failure, unsupported operation, deterministic failure, scope or authority boundary]
Runtime artifacts: [environment, dependencies, caches, generated outputs, receipt retention, and authorized cleanup envelope]
Execution order: [wrapper ValidateOnly | AGY semantic/remediation phase | runtime materialization | focused checks | broad gate]
Objective-specific probe: [required non-empty diff, final files/directories, structural metrics, or value-equivalence evidence]
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
Semantic probes: [outcome-specific boundary values, least-privilege reachability,
reversible state transitions, and adjacent negative controls that apply]
Language: [requested language or inherit]

Do not implement fixes or broaden scope. Return evidence and an accept or needs_followup recommendation.
```

The reviewer profile comes from the role table in `../SKILL.md`; it does not
require creating a reviewer. Start one only when risk or repository policy
warrants it and the review readiness gate passes. Populate its prompt
from the compact acceptance packet; do not attach worker chat, full Issue history,
or raw logs when stable evidence locations are available.

Do not ask the reviewer to rerun the frozen repository-wide gate solely to add an
actor. Review the immutable target and test evidence, then exercise the
decision-critical semantic risks that the broad suite may not cover.

## Parallel pilot

```text
Use $task-conductor for a controlled parallel pilot.

Durable trackers: [trackers]
Authorized concurrency: Up to [2] mutating workers under [authorization]; no nested tasks.
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
Delivery cutoff: [accepted manifest, immutable target, timestamp, and frozen telemetry]
Explicit hard limits: [user/repository limits; omit if none]
Stop conditions: [completion, failed preflight, material drift, no progress, authority or explicit hard-limit boundary]
Language: [requested language or inherit]

Do not change accepted delivery scope. Return the completion contract and keep this
operation outside the delivery-acceptance measurement boundary.
```

For production cutovers, make health gates enumerate every required dependency and
test platform-dependent assertions against representative output before mutation.
Do not use production retries as the primary parser, quoting, or assertion test
harness.
