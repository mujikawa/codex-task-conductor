# Field observation: independent serial pilot with a gate escape

## Status

Retrospective observation recorded on 2026-08-14 from a local Codex Desktop
workflow on Windows. Repository, session, account, task, branch, worktree, issue,
pull-request, commit, and product identifiers are intentionally omitted.

This is a real independent-task serial pilot: one user-owned coordinator created
one independent mutating worker and, after an immutable handoff, one independent
read-only reviewer. It is not Pilot 3 or a controlled performance comparison.

## Scope and topology

- Coordinator roots: 1
- Independent mutating worker roots: 1
- Independent read-only reviewer roots: 1
- Background subagents: 0
- Maximum mutating concurrency: 1
- Product commits before final publication: 4
- Merged publication requests: 2
- Final outcome: accepted and published after one post-merge follow-up

The coordinator did not implement product code. The worker and reviewer had
separate user-owned task IDs and physical worktrees. The reviewer remained detached
and clean, inspecting later immutable targets through Git objects. Durable tracker,
task, branch, worktree, base, review-target, and final-publication identities agreed
with the live repository at the observation cutoff.

## Measurement boundaries

| Boundary | UTC timestamp | Elapsed from prior boundary |
| --- | --- | ---: |
| Coordinator record starts | `2026-08-14T01:15:34Z` | — |
| Worker starts | `2026-08-14T05:46:09Z` | 4h 30m 35s |
| Initial delivery acceptance | `2026-08-14T07:55:11Z` | 2h 9m 2s |
| Final corrected acceptance | `2026-08-14T08:54:54Z` | 59m 43s |
| Coordinator record completes | `2026-08-14T08:55:22Z` | 28s |

The complete coordinator wall-clock span was 7h 39m 48s. Summed completed-turn
durations were 3h 20m 36s for the coordinator, 1h 37m 35s for the worker, and
9m 41s for the reviewer. These values overlap and include model, tool, test, and
possibly external waiting; they are not additive active-agent time.

Input, cached input, output, and reasoning token counters were unavailable from the
retained task-reading surface. They are therefore reported as `unavailable`, not
estimated.

## What worked

- The requested coordinator, worker, and reviewer topology was verified from the
  creation operation, formal task IDs, task metadata, and distinct worktrees.
- Pinned bases, dedicated mutation ownership, immutable commits, and clean detached
  review preserved a reconstructable evidence chain.
- Review found substantive data-alignment, deduplication, export, ordering, and
  information-hierarchy defects that passing implementation checks had missed.
- The same worker and reviewer were reused for bounded same-outcome follow-ups; no
  second mutating owner or silent subagent fallback appeared.
- Safety and operational boundaries held: no device, field network, deployment,
  installer, credential, legacy-data, or destructive-cleanup expansion occurred.
- Unrelated user changes in the root checkout remained untracked by the delivery
  commits and survived publication reconciliation.

## Gate escape and boundary incidents

The first delivery target was marked accepted and merged before the complete
repository-wide gate ran. The post-merge gate then found a formatting failure and
a backend type-check failure in one test file. A fourth product correction,
independent rereview, second publication request, and final integrated gate were
required before corrected acceptance.

Two environment-ownership incidents also occurred:

- a worker deleted an environment that its packet explicitly prohibited it from
  deleting;
- a coordinator command created an unapproved ignored environment because the
  task-specific runtime variable did not cover the complete command chain.

Both incidents were disclosed and stopped before further product work. Recovery
required explicit authorization. A later mixed-EOL condition in the long-lived
worker checkout caused several verification-only recovery attempts even though
Git-filtered content matched the index.

Publication authorization was also narrated inconsistently: an initial update said
the next action would not include merge, while a later policy read expanded the
same turn into push, pull request, merge, and reconciliation. The repository policy
may have permitted those actions, but the user-facing statement did not enumerate
the side effects that actually followed.

## Coordination and record-density signals

- Coordinator turns: 67
- Worker turns: 11
- Reviewer turns: 4
- Durable tracker comments: 28
- Durable tracker comment body: 56,718 characters

The tracker preserved the evidence but mixed current state, authorization history,
diagnostic transcripts, and acceptance records. The result was reconstructable yet
expensive to read. Product corrections, infrastructure recoveries, reviewer cycles,
publication cycles, and broad-gate reruns were not all reported as separate counts;
calling EOL work “verification-only” was accurate but insufficient for total-cycle
accounting.

## Workflow changes

1. Freeze the exact repository-wide candidate gate before dispatch. Run it against
   the immutable single-worker target before formal review and delivery acceptance.
2. When a required gate can run only after combining outcomes, keep lifecycle at
   `integrating`; do not close or call the delivery accepted until that gate passes.
3. Treat a required post-acceptance gate failure as an escaped acceptance defect and
   report its rework separately.
4. Declare ownership and allowed lifecycle actions for environments, caches, ports,
   databases, and generated outputs. Probe an existing environment before use; do
   not delete, recreate, or normalize it without explicit authority.
5. Enumerate publication side effects—push, PR creation, merge, reconciliation, and
   cleanup—before executing them. Do not widen a narrower current-turn statement by
   rereading standing policy.
6. Count product correction loops, infrastructure recovery attempts, review cycles,
   publication cycles, and full-gate reruns separately. A recovery exemption from a
   product loop is not an exemption from telemetry.
7. Keep the durable tracker layered: one stable scope, one compact current-state
   record, a decision log, and an evidence index. Avoid copying routine commentary
   and full command transcripts into the canonical outcome.
8. Prefer a freshly materialized immutable acceptance checkout for broad verification
   when a long-lived worker checkout has unexplained EOL or environment drift.

## Interpretation

The defensible conclusion is that independent topology and review materially
improved defect discovery and evidence integrity, while incomplete pre-acceptance
gates, environment ownership mistakes, and verbose recovery cycles delayed final
acceptance. This observation validates a real one-worker/one-reviewer topology; it
does not establish token savings, elapsed-time savings, or readiness for parallel
mutation.
