# Task Conductor

Keep the coordinator light, give every worker one score, and accept evidence—not applause.

A draft, reusable Codex skill for coordinating tracked delivery across bounded workers without making one long-running session the only source of truth. Coordinator-owned subagents are the primary automation layer; independent user-owned tasks remain available for material lifecycle boundaries.

## Motivation

This workflow originated from an observed long-running delivery session where coordination, implementation, repeated verification, and growing context were handled in one high-reasoning task. The work produced useful results, but token use and elapsed time grew substantially.

The observation does not prove that a particular model or reasoning level caused the cost. Long context, repeated state reads, tool and test waits, implementation scope, and rework were also plausible contributors. This project turns those observations into measurable workflow controls:

- keep coordinators focused on dependencies and acceptance
- dispatch one bounded outcome per worker
- use subagents for outcome-level automation and durable tracker checkpoints for coordinator context rollover
- isolate mutating work with dedicated branches and worktrees
- require durable handoffs and evidence-based acceptance
- gate concurrency before claiming safe parallel work
- record model, reasoning effort, tokens, elapsed time, waits, and reruns when telemetry exists

## Status

This repository is the `v0.1.1-preview` release. The generic skill, adoption guidance,
MIT license, release checklist, two serial observational case studies, and four
field observations are present.

The workflow has been exercised with serial independent tasks, a clean-room
coordinator-owned subagent, and a controlled two-worker concurrent pilot with an
integration acceptance gate. A published-tag reinstall and fresh-process
recognition smoke test have also passed. The optional `$delegate-to-agy` executor
contract now has one accepted clean-room pilot after its wrapper and portable EOL
boundaries were corrected. The evidence remains preliminary: the successful run
followed explicit replacement-worker authorization and one service-level fresh
retry, so it validates the bounded workflow rather than reliability or efficiency.

## Layout

```text
skills/task-conductor/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   └── task-governance-template.md
└── references/
    ├── context-loading.md
    ├── delegate-to-agy.md
    ├── git-isolation.md
    ├── measurement.md
    ├── parallel-readiness.md
    ├── status-contract.md
    ├── task-prompts.md
    └── troubleshooting.md

docs/
├── adoption.md
├── case-study.md
├── field-observation-long-lifecycle.md
├── field-observation-subagent-parallel-agy.md
├── field-observation-serial-gate-escape.md
├── field-observation-zero-dispatch.md
├── release-v0.1.0-preview.md
├── release-v0.1.1-preview.md
└── release-checklist.md

CHANGELOG.md
LICENSE
```

## Core safety properties

- Worker creation, topology, concurrency, and external mutations require explicit user authorization.
- Coordinator-owned subagents are preferred for bounded automation; independent tasks are reserved for material user-owned lifecycle boundaries.
- Worker ownership and implementation executor are separate: an explicitly authorized Codex worker may manage AGY through the separately installed `$delegate-to-agy` skill.
- Every mutating worker owns a dedicated branch and physical worktree.
- Parallel dispatch requires independent outcomes, frozen contracts, non-overlapping mutation scopes, isolated resources, and an integration gate.
- Worker summaries are not acceptance evidence.
- Dispatch and acceptance use compact packets guarded by context, review-readiness,
  and model/tool-cycle budgets.
- Missing telemetry is reported as unavailable, never estimated.

## Adoption and prerequisites

Read the [adoption guide](docs/adoption.md) before a team rollout. It explains the boundary between optional global guidance, shared repository instructions, task governance, and the reusable skill. It also provides capability fallbacks for environments without task creation, bounded monitoring, model overrides, worktrees, or a durable tracker.

Copy and tailor the [task-governance template](skills/task-conductor/assets/task-governance-template.md) only when the target repository does not already have an equivalent policy. Repository policy remains authoritative.

## Installation

Ask Codex to use `$skill-installer` to install the `skills/task-conductor`
directory from [mujikawa/codex-task-conductor](https://github.com/mujikawa/codex-task-conductor).

For a reproducible release installation, ask:

```text
Use $skill-installer to install skills/task-conductor from
mujikawa/codex-task-conductor at ref v0.1.1-preview.
```

Restart or reload Codex after installation, then open a fresh task and ask:

```text
List the active task-conductor skill, summarize when it is allowed to create
independent tasks, and do not dispatch anything.
```

If the skill is not recognized, verify that the installed directory contains `SKILL.md` at its root and that its frontmatter name is `task-conductor`.

Invoke the installed skill as `$task-conductor`. Repository instructions remain authoritative for branch lifecycle, verification commands, durable trackers, language, and owner-only actions.

## Optional AGY executor

Task Conductor can use `$delegate-to-agy` as an optional implementation executor
without bundling or copying that skill. Install and maintain `$delegate-to-agy`
separately. Explicitly invoking Task Conductor alone does not authorize sending
workspace code to AGY.

The recommended ownership chain is one coordinator-owned Codex worker subagent
managing one AGY implementation in a clean linked worktree. The Codex worker
captures the baseline, invokes AGY, independently reviews the actual diff, runs
validation, and returns evidence to the coordinator. AGY remains an executor, not
a Codex task, reviewer, or durable owner. See the
[AGY executor integration contract](skills/task-conductor/references/delegate-to-agy.md).

## First subagent-first serial pilot

Start in a fresh coordinator task with a prompt similar to:

```text
Use $task-conductor for one serial pilot. You may spawn and monitor exactly one
coordinator-owned worker subagent for [bounded outcome]. Use [tracker] as durable
state. Do not create an independent task, nested subagent, or second worker.
Require [verification gate], then independently accept or reject the evidence and
stop.
```

The coordinator should show a compact dashboard containing the outcome,
dependency, topology and routing ID, execution profile, isolation, state,
evidence, and one next action. It should not implement the worker's assigned
scope.

To stop, tell the coordinator to stop dispatching, preserve durable handoff state,
and report all active agent paths and independent task IDs. Subagents are
parent-owned; independent tasks are user-owned and may need to be stopped or
archived separately. Never switch between them silently.

## Known limitations

- The recorded pilots are observational, not controlled efficiency benchmarks.
  Their different outcome scopes prevent direct token or elapsed-time comparison.
- One controlled two-worker clean-room pilot passed readiness, isolated delivery,
  and ordered integration acceptance. It does not establish performance gains or
  prove hardware-level simultaneous execution.
- Codex task-management, model override, monitoring, and worktree capabilities vary by surface and host.
- Token telemetry is cumulative and requires an explicit snapshot cutoff to avoid mixing later dispatches into an earlier baseline.
- Automatic review and background subagent sessions can add hidden descendants; topology must be classified by the creation path and lineage, not a single metadata label.
- Sidebar placement does not establish ownership: a surfaced subagent thread may look like a task while remaining parent-owned.
- Codex context rollover and compaction thresholds are not treated as a fixed product contract. Checkpoint durable state before rollover and adopt it without redispatching active workers.
- `$delegate-to-agy` is an optional external dependency. Its wrapper, policy, authentication, and installation lifecycle are not bundled with this repository.
- The first Task Conductor plus AGY clean-room attempt exposed a cross-identity
  Git inspection defect in the separately maintained wrapper. After that defect
  was repaired and reinstalled, a later AGY run returned `SUCCESS` but failed the
  exact-LF acceptance check. A second wrapper repair admitted the valid
  same-conversation remediation, but AGY returned terminal `ERROR` after leaving
  the correct LF artifact. A later bounded fresh run returned `SUCCESS` with a
  current receipt but again materialized CRLF. A newly scoped pilot then adopted
  repository-owned LF policy and immutable-blob acceptance. After one zero-change
  `503 UNAVAILABLE` and the single permitted fresh retry, AGY returned `SUCCESS`;
  Codex verified the receipt, scope, exact 9-byte committed blob, ancestry, and
  tracked-clean state before acceptance.
- Recent-task inventory is bounded and may not prove exclusive ownership by itself. A rejected inventory query means ownership is unknown, not conflicting or clear.
- A newly created task may exist and start before recent-task inventory exposes its formal ID. A client-side creation handle proves acceptance, while setup and execution remain unknown until directly verified.
- Long initiatives can defeat bounded orchestration when later publication,
  infrastructure, credential, policy, deployment, and cleanup work remain in the
  original feature task. Use explicit lifecycle cutoffs and new outcomes.

The [long-lifecycle field observation](docs/field-observation-long-lifecycle.md)
records a retrospective lower-bound telemetry analysis and the workflow changes it
motivated. It is not a controlled comparison with the serial pilots.

The [zero-dispatch field observation](docs/field-observation-zero-dispatch.md)
records a complete single-root manual-serial baseline. It distinguishes Git and
tracker isolation from actual independent-task topology and is also not a
controlled comparison with the serial pilots.

The [serial gate-escape field observation](docs/field-observation-serial-gate-escape.md)
records a real coordinator, independent worker, and independent reviewer topology
that ultimately succeeded but required post-merge correction after an incomplete
candidate gate. It motivates stricter acceptance, runtime-ownership, publication,
and cycle-accounting rules.

The [subagent, parallel, and AGY clean-room field observation](docs/field-observation-subagent-parallel-agy.md)
records the first direct subagent acceptance, a controlled two-worker integration,
and the bounded AGY recovery sequence through the first accepted portable-EOL AGY
delivery without treating partial or byte-invalid output as accepted evidence.

See the [release checklist](docs/release-checklist.md) before tagging or publishing a release.
See the [v0.1.1-preview release notes](docs/release-v0.1.1-preview.md) for the
latest validation evidence and usage guidance. The
[v0.1.0-preview notes](docs/release-v0.1.0-preview.md) remain available for the
original topology rationale and examples.
For destination, inventory, ownership, or topology failures, use the [dispatch troubleshooting guide](skills/task-conductor/references/troubleshooting.md).

## License

Released under the [MIT License](LICENSE).
