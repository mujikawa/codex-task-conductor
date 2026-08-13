# Case studies: Task Conductor serial pilots

## Status

Corrected observational baseline recorded on 2026-08-11 from local Codex Desktop telemetry on Windows. Identifiers and repository-specific details are intentionally omitted. This is not an efficiency comparison or controlled benchmark.

The original draft used the coordinator's later cumulative counter and therefore mixed post-pilot dispatch activity into the first four outcomes. This revision freezes the snapshot at the fourth outcome decision and separates completed outcomes from accepted outcomes.

## Motivation

An earlier long-running delivery task accumulated coordination, implementation, repeated repository inspection, verification, external-state checks, and handoff work. That experience motivated a bounded coordinator workflow.

The earlier task is not a valid comparison baseline because its scope, outcome count, task topology, and reasoning effort differed from Pilot 1. Its measurements are excluded from the performance table and retained only as historical motivation.

Task Conductor starts with three hypotheses to test in future comparable runs:

1. separating coordination from implementation reduces repeated context processing
2. bounded worker prompts reduce irrelevant history carried into each outcome
3. execution profiles and bounded monitoring make token/latency tradeoffs visible

Pilot 1 does not establish any of these hypotheses causally.

## Pilot 1 scope and cutoff

Pilot 1 used one coordinator and four serially dispatched independent tasks. Four bounded worker outcomes completed: three were accepted and one returned `needs_followup`. It did not test parallel execution.

The execution profile was `gpt-5.6-sol medium` for the coordinator and direct workers, with automatic review at `low`. The snapshot contains 12 sessions: one coordinator, four direct worker tasks, and seven automatic-review descendants.

- Start: `2026-08-11T02:42:17.802Z`
- Cutoff: `2026-08-11T06:29:16.368Z`, the fourth outcome decision
- Later coordinator dispatches: excluded

## Operational baseline

| Measure | Pilot 1 value |
| --- | ---: |
| Completed bounded outcomes | 4 |
| Accepted outcomes | 3 |
| `needs_followup` outcomes | 1 |
| Coordinator tasks | 1 |
| Direct independent worker tasks | 4 |
| Automatic-review descendants | 7 |
| Total sessions included | 12 |
| Input tokens | 76,104,468 |
| Cached input tokens | 73,217,536 |
| Uncached input tokens | 2,886,932 |
| Output tokens | 178,184 |
| Reasoning output tokens | 44,683 |
| Total reported tokens | 76,282,652 |
| Wall-clock workflow window | 3h 46m 59s |
| Summed session spans | 7h 39m 43s |
| Active model time | unavailable |
| Tool and test wait time | unavailable |
| Final snapshot result | 4 completed; 3 accepted; 1 `needs_followup` |

`Summed session spans` adds each included session's first-to-last timestamp, truncating cumulative coordinator telemetry at the cutoff. It includes overlap, idle periods, tool waits, and review waits, so it is only a workload-span proxy and not compute time.

## Token distribution

| Workflow component | Tokens | Share |
| --- | ---: | ---: |
| Coordinator | 38,252,176 | 50.1% |
| Direct independent workers | 34,268,426 | 44.9% |
| Automatic review | 3,762,050 | 4.9% |
| Total | 76,282,652 | 100.0% |

The coordinator share is the main optimization signal for the next comparable pilot. Future runs should test whether compact durable status, fewer repeated reads, and bounded acceptance reduce this share without weakening evidence quality.

## Per-outcome normalization

Session count is an implementation detail rather than delivered value. Completed and accepted denominators answer different questions and must not be conflated.

| Derived measure | Pilot 1 value |
| --- | ---: |
| Workflow tokens per completed bounded outcome | 19,070,663 |
| Workflow tokens per accepted outcome | 25,427,551 |
| Direct-worker tokens per completed bounded outcome | 8,567,107 |
| Coordinator / workflow tokens | 50.1% |
| Automatic review / workflow tokens | 4.9% |
| Reasoning / total tokens | 0.059% |
| Uncached input / input tokens | 3.79% |

The outcomes were not identical in size, so these averages are portfolio-level indicators, not estimates for an individual task.

## Pilot 1 content-loading profile

Cumulative input is repeated processing across model and tool cycles, not a count of unique content. At the frozen cutoff, 96.2% of Pilot 1 input was cached.

| Component | Input | Cache ratio | Uncached input | Counter increments | Median call input | Maximum call input | Compactions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Coordinator | 38,183,031 | 97.2% | 1,081,975 | 338 | 122,745 | 231,444 | 1 |
| Four independent workers | 34,168,939 | 97.8% | 745,835 | unavailable | unavailable | unavailable | unavailable |
| Automatic review | 3,752,498 | 71.8% | 1,059,122 | 79 | 42,079 | 98,211 | 0 |
| Total | 76,104,468 | 96.2% | 2,886,932 | unavailable | — | — | unavailable |

`Counter increments` counts distinct cumulative token-counter advances and is only a proxy for model/tool cycles. Two of four worker root JSONL files were no longer present in active or archived local storage at reanalysis time. The complete worker aggregate remains derivable from the frozen total after subtracting the retained coordinator and all seven automatic-review sessions, but per-call distribution and compaction cannot be reconstructed without extrapolation. Two retained worker roots showed 122 increments, a 98,199 median call input, a 146,712 maximum, and no compaction; these partial values are intentionally excluded from the complete-group table.

The coordinator's maximum call input reached 89.6% of the observed 258,400-token runtime context window. Automatic review represented 4.9% of total reported tokens but 36.7% of uncached input.

## Topology audit

A later audit found a topology transition after the serial baseline. One independent-task creation failed because its saved-project identifier could not be resolved; the coordinator then used a background subagent as a fallback. Its following four dispatches also directly used background subagents, so all five later workers were parent-owned agents rather than independent user-owned tasks.

Those five subagents are excluded from this Pilot 1 snapshot and the unapproved topology transition is now treated as a governance defect. Independent tasks and subagents differ in ownership, visibility, cancellation, context inheritance, and lifecycle. Future runs must stop on task-creation failure unless the user separately authorizes the changed topology, and must re-check the creation operation on every dispatch rather than assuming the first topology remains in effect.

The audit also found that a generic metadata value such as `thread_source: subagent` was present on independent task records. It is therefore not a reliable classifier by itself. Creation operations, returned task IDs, parent lineage, spawn events, and agent paths provide stronger evidence.

A later ownership preflight exposed a separate inventory failure: the coordinator requested more recent tasks than that runtime allowed, so the listing was rejected before ownership could be checked. The project lookup still exposed an ambiguous saved-project destination, but these were different failure dimensions. The corrected rule treats rejected inventory as `unknown`, refreshes it within the current runtime bound, and combines it with known task IDs, Git worktree state, and durable ownership records. The observed bound is not published as a permanent Codex guarantee.

The recovery path then succeeded without deleting duplicate project metadata. The user explicitly selected one destination, the coordinator refreshed and matched it to the expected repository, and task, Git, tracker, and resource ownership all classified as `clear`. A single independent-task creation request returned a client-side creation handle. Local telemetry later showed that the formal task record appeared about 14 seconds after that response and that the worker started normally, yet repeated bounded recent-task snapshots did not expose the formal ID to the coordinator. The user later supplied the ID visible in the UI, after which metadata verification and monitoring worked. The coordinator's earlier statement that setup was still incomplete was therefore too strong: the evidence supported `creation accepted / formal ID unresolved / execution unknown`. This establishes a visibility and correlation race observed in one runtime; it does not identify the internal cause or claim that duplicate project metadata is harmless in every environment.

## Interpretation

Pilot 1 establishes what one bounded serial Task Conductor workflow cost. It does not show that Task Conductor saved tokens or time relative to the earlier long-running task.

A defensible statement is:

> At the fixed fourth-outcome cutoff, the first Task Conductor pilot completed four bounded outcomes—three accepted and one needing follow-up—using 76,282,652 aggregate reported tokens over a 3h 46m 59s workflow window. This is an operational baseline for future comparable pilots, not evidence of savings against the motivating task.

## Requirements for a future comparison

Compare Pilot 1 with another run only when the runs are sufficiently aligned on:

- outcome count, scope, and dependency complexity
- model and reasoning effort
- acceptance and verification gates
- environment and tool availability
- serial or parallel execution topology
- treatment of automatic reviews, retries, and rework
- start and cutoff boundaries used for tokens and elapsed time

Report aggregate tokens, tokens per completed and accepted outcome, wall-clock time, coordinator share, review share, rework, and failed acceptance. State any remaining differences before reporting a change percentage.

## Pilot 2: complete serial delivery

Pilot 2 was recorded on 2026-08-12 from the same local Codex Desktop environment. It followed one customer-facing frontend outcome from initial analysis through a specification, one independent mutating worker, one independent read-only reviewer, evidence acceptance, Git lifecycle, and a separately authorized production deployment. Identifiers, repository names, Issue and PR numbers, product details, and deployment destinations are omitted.

This run used serial orchestration because the UI, calculation, PDF, and test changes shared one contract and overlapping files. Parallel mutation would not have passed the readiness gate.

### Delivery acceptance boundary

The primary measurement starts when the user authorized dispatch and stops when the reviewer evidence was accepted. Earlier analysis and specification work remain visible in the end-to-end window but are not included in the dispatch-to-acceptance duration.

| Measure | Pilot 2 value |
| --- | ---: |
| Accepted bounded outcomes | 1 |
| Coordinator tasks | 1 |
| Independent mutating worker tasks | 1 |
| Independent read-only reviewer tasks | 1 |
| Automatic-review descendants | 4 |
| Total sessions included | 7 |
| Input tokens | 40,072,866 |
| Cached input tokens | 38,279,552 |
| Uncached input tokens | 1,793,314 |
| Output tokens | 102,855 |
| Reasoning output tokens | 21,349 |
| Total reported tokens | 40,175,721 |
| Dispatch authorization to acceptance | 1h 35m 55s |
| Initial request to acceptance | 1h 50m 32s |
| Active model time | unavailable |
| Tool and test wait time | unavailable |
| Final delivery result | accepted |

### Delivery token distribution

| Workflow component | Tokens | Share |
| --- | ---: | ---: |
| Coordinator | 15,519,347 | 38.6% |
| Independent mutating worker | 19,136,095 | 47.6% |
| Independent read-only reviewer | 4,597,189 | 11.4% |
| Automatic review | 923,090 | 2.3% |
| Total | 40,175,721 | 100.0% |

Uncached input was 4.47% of reported input tokens. Reasoning output was 0.053% of total reported tokens.

### Delivery content-loading profile

| Component | Input | Cache ratio | Uncached input | Counter increments | Median call input | Maximum call input | Compactions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Coordinator | 15,484,213 | 96.8% | 500,789 | 125 | 118,579 | 188,781 | 0 |
| Independent mutating worker | 19,085,382 | 97.8% | 418,118 | 155 | 120,960 | 224,406 | 1 |
| Independent read-only reviewer | 4,583,306 | 93.6% | 291,594 | 47 | 100,466 | 152,462 | 0 |
| Automatic review | 919,965 | 36.6% | 582,813 | 23 | 41,076 | 64,075 | 0 |
| Total | 40,072,866 | 95.5% | 1,793,314 | 350 | — | — | 1 |

The automatic-review row pools calls from four short sessions. Automatic review represented 2.3% of total reported tokens but 32.5% of uncached input.

The worker reached 86.8% of the observed 258,400-token runtime context window and compacted once. The coordinator reached 73.1% by delivery acceptance without compaction; it later reached 89.2% and compacted during the separately authorized deployment phase.

### Separate lifecycle boundaries

Git publication and production deployment required later user authorizations and are not part of the delivery-acceptance snapshot. Their counters are reported cumulatively and incrementally so later operational work is not silently attributed to implementation.

| Boundary | Cumulative tokens | Increment since prior boundary | Authorized phase duration |
| --- | ---: | ---: | ---: |
| Delivery accepted | 40,175,721 | — | 1h 35m 55s from dispatch |
| Git lifecycle complete | 46,941,979 | 6,766,258 | 6m 55s |
| Production deployment complete | 48,565,947 | 1,623,968 | 7m 21s |

The final end-to-end window from the initial request through deployment was 2h 6m 51s. Phase durations are wall-clock windows for the corresponding authorized turns; they do not measure active model or compute time.

### Interpretation

Pilot 2 demonstrates that the workflow can preserve a user-owned coordinator, independent worker, independent reviewer, dedicated Git isolation, evidence acceptance, and later operational authorization through a complete serial delivery. The four background sessions were classified separately as automatic-review descendants rather than coordinator-dispatched workers.

The coordinator share was lower than Pilot 1's 50.1%, but this is not evidence of a 23% efficiency improvement. Pilot 1 contained four heterogeneous outcomes, while Pilot 2 contained one larger outcome with specification work, PDF visual verification, independent review, Git lifecycle, and deployment. Raw totals and per-outcome values are therefore not directly comparable.

The content profiles suggest that the lower coordinator total was driven more by fewer coordinator cycles than by a much smaller context per cycle: the observed counter increments fell from 338 to 125 while median call input changed from 122,745 to 118,579. Because the pilots differ in outcome count and scope, this is a workload-shape observation rather than an efficiency claim.

Across both pilots, automatic review consumed a small share of total tokens but a disproportionate share of uncached input. This supports tracking review initialization separately rather than treating every background session as inexpensive cached continuation.

Official OpenAI model guidance recommends tracking cached tokens separately and notes that long sessions can amplify repeated prompt and tool content. These case studies apply that interpretation to observed Codex Desktop telemetry; they do not claim that uncached input equals semantically unique information. See [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model).

A defensible cross-pilot observation is:

> In a second serial pilot with one accepted outcome, the delivery-acceptance boundary used 40,175,721 aggregate reported tokens over 1h 35m 55s from dispatch authorization. Coordinator share was 38.6%, and topology remained one independent worker plus one independent reviewer. This is evidence that the workflow completed end to end, not evidence that it reduced token use or elapsed time.

## Calculation method

- Freeze the exact start and declared acceptance cutoff before reading cumulative counters.
- Include the declared coordinator, independent worker and reviewer roots, and descendants recursively linked by parent lineage that started before the cutoff.
- Read active and archived local session JSONL files.
- Use the last cumulative `event_msg.token_count` record at or before the cutoff for every included session.
- Count distinct cumulative-token advances only as a proxy for model/tool cycles.
- Report per-call distribution and compaction as unavailable when any included root telemetry is no longer retained; do not extrapolate from surviving roots.
- Group components by creation and lineage evidence rather than the generic `thread_source` field.
- Sum token categories without estimating missing telemetry.
- Use cutoff minus coordinator start for the end-to-end wall-clock window.
- Keep session identifiers in an ignored local source map; do not publish raw JSONL files or conversation content.

## Publication gate

Before publishing comparative conclusions:

- compare equivalent outcomes and validation gates
- record environment, observation date, and exact cutoff
- distinguish independent tasks, subagents, and automatic-review descendants
- distinguish completed, accepted, and follow-up outcomes
- distinguish wall-clock, active work, and wait time when possible
- keep token categories separate
- label unavailable telemetry explicitly
- report observations separately from causal claims
- remove session IDs, private repository names, issue numbers, customer data, production details, and credentials

## Pilot 3: planned observational validation

Pilot 3 will validate the context-loading workflow controls rather than treat Pilot
1 or Pilot 2 as a direct efficiency comparator. It will pre-register an equivalent
outcome and acceptance gate where practical, then record compact dispatch and
acceptance packet size and completeness, context-budget and review-readiness
decisions, declared and observed cycle budgets, repeated broad reads or reruns, and
exceptions to the diff, test, Issue, and artifact reduction rules.

The pilot will also record acceptance quality, follow-up and rework, component-level
context telemetry when available, and whether post-acceptance work stopped or moved
to an explicitly authorized independent Ops task with a separate packet and cutoff.
Missing telemetry will remain `unavailable`. Results will be reported as observed
workflow behavior unless all comparison requirements above are met.

## Early lesson

The coordinator pattern is not automatically cheaper. Additional tasks may improve isolation or reduce wall-clock time while increasing aggregate tokens. Its primary promise is bounded context, clearer ownership, safer orchestration, and independently verifiable delivery; efficiency requires comparable evidence.
