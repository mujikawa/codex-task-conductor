# Field observation: zero-dispatch serial delivery

## Status

Retrospective observation recorded on 2026-08-14 from a local Codex Desktop
workflow on Windows. Repository, session, account, host, branch, issue,
pull-request, commit, and product identifiers are intentionally omitted.

This is not Pilot 3, a controlled comparison, or a successful independent-task
pilot. It is a **manual serial Task Conductor adoption / zero-dispatch baseline**:
one user-owned root task applied durable tracking and Git isolation while the same
agent performed coordination, implementation, review, integration, and handoff.

## Scope and topology

The root began as software archaeology and later expanded into repository setup,
governance adoption, application modernization, packaging, acceptance, Git
publication, and an authorization-gated operational handoff.

- Accepted bounded outcomes: 17
- Blocked operational outcomes: 1
- Independent Codex worker tasks: 0
- Background subagents: 0
- Root coordinator tasks: 1
- Repository commits produced across the observed initiative: 47
- Merge commits: 10

The user authorized durable Issue tracking and later Git publication, merge, and
reconciliation. The retained record did not contain explicit authorization to
create independent Codex tasks. Not dispatching was therefore consistent with the
authorization boundary. The governance defect was describing coordinator-owned
manual execution as `Worker`, and procedurally isolated self-review as an
independent `Reviewer`.

## Measurement boundaries

The primary delivery window starts when execution of the tracked outcome graph was
authorized and stops when corrected delivery evidence was accepted and the next
operational outcome was recorded as blocked. Earlier discovery and repository
preparation remain separate; two later support questions are excluded from
delivery.

| Boundary | UTC timestamp | Treatment |
| --- | --- | --- |
| Root record starts | `2026-08-12T16:00:59.998Z` | End-to-end observation only |
| Tracked execution starts | `2026-08-13T03:27:21.958Z` | Primary delivery start |
| Offline delivery accepted | `2026-08-13T09:23:10.263Z` | Intermediate product cutoff |
| Corrected online delivery accepted | `2026-08-13T14:39:20.006Z` | Primary delivery cutoff |
| Final support turn completes | `2026-08-14T01:12:51.267Z` | Excluded from delivery |

Token boundaries use the last cumulative counter at or before each timestamp.
Reasoning output is a diagnostic subset of output usage and is not added a second
time to reported totals.

## Primary delivery measurement

| Measure | Value |
| --- | ---: |
| Authorization to corrected acceptance | 11h 11m 58s |
| Completed-turn elapsed inside that window | 8h 14m 28s |
| Model/tool-cycle proxy | 1,658 |
| Input tokens | 219,188,197 |
| Cached input tokens | 213,431,936 |
| Uncached input tokens | 5,756,261 |
| Output tokens | 827,317 |
| Reasoning output tokens | 230,945 |
| Context compactions | 12 |
| Delivery result | 17 accepted; 1 operational outcome blocked |

Completed-turn elapsed includes model, tools, tests, and some human or external
waiting. It is not active model time. Active work, tool/test wait, and human wait
cannot be separated authoritatively from the retained telemetry.

## Full-root telemetry

| Measure | Value |
| --- | ---: |
| Root-record wall clock | 33h 11m 51s |
| Completed-turn elapsed | 9h 50m 50s |
| Completed / aborted turns | 49 / 3 |
| Model/tool-cycle proxy | 2,003 |
| Input tokens | 255,217,754 |
| Cached input tokens | 247,719,040 |
| Uncached input tokens | 7,498,714 |
| Cache ratio | 97.06% |
| Output tokens | 1,035,275 |
| Reasoning output tokens | 298,995 |
| Context compactions | 15 |

The high cache ratio does not make repeated cycles free and does not turn
cumulative input into unique content. It shows that a large conversation and tool
prefix was repeatedly processed with substantial cache reuse.

## Phase profile

| Phase | Wall clock | Cycle proxy | Input | Uncached input | Output | Compactions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Discovery, planning, repository preparation | 11h 26m 22s | 338 | 35,179,355 | 1,506,907 | 204,089 | 3 |
| Tracked offline outcomes | 5h 55m 48s | 1,072 | 141,021,712 | 3,279,760 | 540,244 | 7 |
| Tracked online and operational handoff | 5h 16m 10s | 586 | 78,166,485 | 2,476,501 | 287,073 | 5 |
| Post-delivery support questions | 10h 33m 31s | 7 | 850,202 | 235,546 | 3,869 | 0 |

The pre-execution and post-delivery wall-clock spans include long user-idle gaps.
They must not be interpreted as continuous agent work.

## Context-loading profile

| Measure | Value |
| --- | ---: |
| Median last-call input | 127,729 |
| P95 last-call input | 218,563 |
| Maximum last-call input | 244,621 |
| Observed context window | 258,400 |
| Maximum context utilization | 94.7% |
| Recorded execution-profile applications | 67 |
| High-reasoning applications | 65 |

One three-hour completed turn crossed several accepted outcomes, Git lifecycle
boundaries, and the start of a later packaging outcome. It compacted five times.
This is direct evidence that durable outcome records and worktree isolation alone
do not keep a root task bounded when implementation stays in the coordinator.

## What worked

- Durable Issues preserved outcome state, dependencies, evidence, and the blocked
  operational boundary.
- Dedicated branches and physical worktrees isolated serial mutation.
- Pinned commits, detached acceptance snapshots, fresh environment rebuilds, and
  artifact hashes made the delivery technically reviewable.
- A later immutable review found a real fresh-process import defect even after the
  broad test gate passed.
- Corrected packaging evidence was regenerated and reviewed instead of accepting
  stale artifact hashes.
- Live-equipment access remained blocked pending a new owner, network, schedule,
  rollback, and stop authorization.

## Cost and rework signals

- The root used 1,887 execution-orchestration calls; 32 ended as wrapper failures
  (1.7%). The scale was driven more by breadth, repeated context, verification, and
  rework than by widespread command failure.
- The packaging outcome produced seven local acceptance-evidence generations
  before corrected delivery acceptance.
- Formal actor-independent review never occurred. Detached snapshots improved
  procedural independence but did not remove shared-agent bias.
- Tracker rows used durable Issue numbers where the Task Conductor status contract
  expected independent task IDs, conflating tracker identity with execution
  topology.
- `S` / `M` / `L` labels did not provide enforceable model/tool cycle budgets.
- Cleanup was deferred. At reanalysis time, 22 auxiliary worktrees remained
  registered; all were clean, but they lacked prompt cleanup classification.

## Workflow changes

1. Before the first `Worker`-labelled outcome, ask separately for authorization to
   create an independent Codex task. If authorization is absent, label the topology
   `manual serial implementation` and do not claim a worker pilot.
2. Keep durable tracker IDs and independent task IDs in separate fields.
3. Use one bounded outcome per task title; start a fresh task when an exploratory
   session becomes a multi-outcome delivery initiative.
4. Keep the coordinator out of implementation scope after worker dispatch, and use
   an actor-independent reviewer when the record claims independent review.
5. Replace size labels with declared model/tool cycle budgets, correction limits,
   and a stop condition.
6. Run fresh-process import and executable-startup checks before packaging so late
   review findings do not invalidate already generated artifacts.
7. Freeze product, publication, operational, and cleanup boundaries separately.
8. Classify accepted worktrees promptly as `retain-for-rollback`, `cleanup-ready`,
   or `dirty-owner-action`.

## Interpretation

The defensible conclusion is that one zero-dispatch root delivered strong Git
isolation, durable evidence, and safe operational boundaries while accumulating
very high context and coordination cost. It does not prove that independent
dispatch would reduce aggregate tokens or elapsed time; additional tasks can add
initialization and review cost. It establishes a complete manual-serial baseline
and a concrete topology audit for a future comparable one-worker pilot.
