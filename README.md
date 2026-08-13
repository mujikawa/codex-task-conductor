# Task Conductor

Keep the coordinator light, give every worker one score, and accept evidence—not applause.

A draft, reusable Codex skill for coordinating tracked delivery across bounded worker tasks without making one long-running session the only source of truth.

## Motivation

This workflow originated from an observed long-running delivery session where coordination, implementation, repeated verification, and growing context were handled in one high-reasoning task. The work produced useful results, but token use and elapsed time grew substantially.

The observation does not prove that a particular model or reasoning level caused the cost. Long context, repeated state reads, tool and test waits, implementation scope, and rework were also plausible contributors. This project turns those observations into measurable workflow controls:

- keep coordinators focused on dependencies and acceptance
- dispatch one bounded outcome per worker
- isolate mutating work with dedicated branches and worktrees
- require durable handoffs and evidence-based acceptance
- gate concurrency before claiming safe parallel work
- record model, reasoning effort, tokens, elapsed time, waits, and reruns when telemetry exists

## Status

This repository is a `v0.1.0-preview` draft. The generic skill, adoption guidance, MIT license, release checklist, and two serial observational case studies are present.

The workflow has been exercised with serial independent tasks. A clean-room installation test and a controlled two-worker parallel pilot are still pending. Parallel orchestration must therefore be described as experimental, not validated.

## Layout

```text
skills/task-conductor/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   └── task-governance-template.md
└── references/
    ├── context-loading.md
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
└── release-checklist.md

CHANGELOG.md
LICENSE
```

## Core safety properties

- Task creation, concurrency, and external mutations require explicit user authorization.
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

Restart or reload Codex after installation, then open a fresh task and ask:

```text
List the active task-conductor skill, summarize when it is allowed to create
independent tasks, and do not dispatch anything.
```

If the skill is not recognized, verify that the installed directory contains `SKILL.md` at its root and that its frontmatter name is `task-conductor`.

Invoke the installed skill as `$task-conductor`. Repository instructions remain authoritative for branch lifecycle, verification commands, durable trackers, language, and owner-only actions.

## First serial pilot

Start in a fresh coordinator task with a prompt similar to:

```text
Use $task-conductor for one serial pilot. You may create and monitor exactly one
independent Codex task for [bounded outcome]. Use [tracker] as durable state.
Do not create subagents or a second worker. Require [verification gate], then
independently accept or reject the evidence and stop.
```

The coordinator should show a compact dashboard containing the outcome, dependency, owner, task title/ID, execution profile, isolation, state, evidence, and one next action. It should not implement the worker's assigned scope.

To stop, tell the coordinator to stop dispatching, preserve durable handoff state, and report all active independent task IDs. Independent tasks are user-owned and may need to be stopped or archived separately. A background subagent is parent-owned and is not an interchangeable fallback.

## Known limitations

- The recorded pilots are observational, serial, and not controlled efficiency benchmarks. Their different outcome scopes prevent direct token or elapsed-time comparison.
- Parallel readiness rules are specified but have not completed a controlled two-worker clean-room pilot.
- Codex task-management, model override, monitoring, and worktree capabilities vary by surface and host.
- Token telemetry is cumulative and requires an explicit snapshot cutoff to avoid mixing later dispatches into an earlier baseline.
- Automatic review and background subagent sessions can add hidden descendants; topology must be classified by the creation path and lineage, not a single metadata label.
- Recent-task inventory is bounded and may not prove exclusive ownership by itself. A rejected inventory query means ownership is unknown, not conflicting or clear.
- A newly created task may exist and start before recent-task inventory exposes its formal ID. A client-side creation handle proves acceptance, while setup and execution remain unknown until directly verified.
- Long initiatives can defeat bounded orchestration when later publication,
  infrastructure, credential, policy, deployment, and cleanup work remain in the
  original feature task. Use explicit lifecycle cutoffs and new outcomes.

The [long-lifecycle field observation](docs/field-observation-long-lifecycle.md)
records a retrospective lower-bound telemetry analysis and the workflow changes it
motivated. It is not a controlled comparison with the serial pilots.

See the [release checklist](docs/release-checklist.md) before tagging or publishing a release.
For destination, inventory, ownership, or topology failures, use the [dispatch troubleshooting guide](skills/task-conductor/references/troubleshooting.md).

## License

Released under the [MIT License](LICENSE).
