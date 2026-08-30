# Task Conductor v0.1.5-preview

This preview converts a seven-subagent vertical-slice delivery into five focused
controls: one immutable-candidate broad-gate owner, semantic review probes,
adaptive monitoring, finite tracker reconciliation, and honest cleanup state.

## Highlights

- Integration selects either a worker-owned or coordinator-owned broad gate
  before dispatch. Independent acceptance no longer repeats the same broad
  commands solely to add another actor.
- Read-only reviewers target outcome-specific boundary values, least-privilege
  reachability, recoverable state transitions, and adjacent negative controls.
- Long tests, builds, and CI use phase-aware wait backoff; unchanged polls are not
  narrated and dense monitoring is measured when telemetry is available.
- One delivery lifecycle normally uses at most one post-merge tracker PR. That
  PR's own merge identifier belongs in its body, comment, or lifecycle receipt,
  not a recursive finalization PR.
- Delivery, publication, reconciliation, and cleanup are separate facets.
  Host-held refs or directories are reported as
  `cleanup-pending-host-release` instead of being force-removed or hidden by a
  generic completion claim.
- Constrained subagent routing paths remain routing data; human-readable worker
  titles stay in dispatch packets and durable trackers.

## Field evidence

The anonymized observation used one serial foundation pilot, two non-overlapping
parallel feature workers, one integration writer, two independent reviewers, and
one bounded correction worker. The final product passed complete repository and
CI gates and merged successfully. The observation also recorded one duplicate
broad-gate boundary, 131 bounded waits, two compactions, three publication PRs,
and safely preserved host cleanup residue.

The frozen ten-root telemetry boundary reported 119,333,142 cumulative tokens,
including 116,100,096 cached input tokens. These counters describe workload
shape, not unique content or proven efficiency impact.

## Install

```text
Use $skill-installer to install skills/task-conductor from
mujikawa/codex-task-conductor at ref v0.1.5-preview.
```

`$delegate-to-agy` remains an optional separately installed dependency. This
release does not change its wrapper or installation contract.

## Release status

This remains a preview. The observed delivery validates bounded orchestration and
review behavior, while the new broad-gate ownership, adaptive monitoring, finite
reconciliation, and lifecycle-facet rules still require a clean forward pilot.
