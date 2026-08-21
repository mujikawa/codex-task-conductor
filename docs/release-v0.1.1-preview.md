# Task Conductor v0.1.1-preview

This preview records the first accepted clean-room coordinator-owned worker, the
first accepted controlled two-worker integration, and the first accepted Task
Conductor worker using the separately installed `$delegate-to-agy` executor.

## What changed

- Coordinator-owned subagents now have forward clean-room evidence for bounded
  delivery and independent coordinator acceptance.
- The controlled two-worker pilot passed isolation, ordered integration, and the
  shared immutable acceptance gate.
- AGY delegation now records a trust-context boundary: the worker that launches
  the external executor must directly inherit explicit user authorization when
  the host approval surface distinguishes trusted user input from coordinator
  relay text.
- Portable exact-text acceptance uses repository-owned EOL policy and immutable
  committed blobs. AGY terminal status and a valid receipt remain necessary but
  are not sufficient acceptance evidence.

The field observation preserves the failed wrapper, terminal-status, receipt,
Windows EOL, authorization-routing, and service-availability stages that preceded
the accepted AGY candidate. One successful pilot does not establish reliability,
token savings, or elapsed-time improvement.

## Installation

Ask Codex:

```text
Use $skill-installer to install skills/task-conductor from
mujikawa/codex-task-conductor at ref v0.1.1-preview.
```

Restart or reload Codex after installation. In a fresh task, ask it to list the
active `task-conductor` skill and summarize its worker-topology and external-AGY
authorization boundaries without dispatching work.

`$delegate-to-agy` remains a separate optional dependency. Task Conductor does
not bundle its wrapper, execution policy, authentication, or runtime state.

## Preview limitations

- A formal task omitted from bounded recent-task inventory has not yet been
  reproduced in a fresh case.
- The post-observation candidate-gate, runtime-ownership, and
  publication-wording guardrails have not yet passed a clean forward pilot.
- The recorded pilots are operational evidence, not controlled efficiency
  benchmarks.

Use this release for controlled adoption and measurement. Keep deployment,
publication, credentials, cleanup, and other lifecycle mutations behind their
own explicit authorization boundaries.
