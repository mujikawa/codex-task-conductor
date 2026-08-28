# Measurement contract

Measure the workflow without turning telemetry into a new source of overhead.

## Record when available

- model and reasoning effort
- input, output, reasoning, and cached tokens as separately reported values
- wall-clock elapsed time
- active agent time and tool/test wait time when distinguishable
- number of worker and follow-up tasks
- repeated full-context reads and full verification reruns
- product correction loops, infrastructure recovery attempts, review cycles,
  publication cycles, and full-gate reruns as separate counters
- conflicts, failed acceptance, and rework
- escaped acceptance defects, including required gates first run or first failing
  after an accepted or published claim
- completed Definition of Done items
- outcome state as `accepted`, `needs_followup`, `blocked`, or another declared status
- creation topology for each root: independent task, background subagent, or manual execution
- implementation executor for each worker: Codex direct or externally delegated

Use `unavailable` for missing telemetry. Do not estimate private reasoning tokens, cached tokens, or active time from wall-clock duration.

## Snapshot boundary

Freeze the measurement boundary before calculating totals:

- record an exact start timestamp and cutoff timestamp
- list the coordinator and worker root task IDs included at that cutoff
- include only recursively linked descendants that started by the cutoff
- for cumulative telemetry, use the last counter at or before the cutoff rather than the session's later final counter
- search both active and archived session storage when the surface moves completed tasks
- keep later dispatches outside an earlier pilot even when they reused the same coordinator
- freeze delivery acceptance before later publication, merge, deployment, or live-operation work begins under separate authorization; report each later phase with its own wall-clock boundary and both cumulative and incremental tokens
- when the initiative materially expands, freeze an additional boundary before
  each new product or infrastructure outcome; do not attribute later provisioning,
  transport, password-policy, credential, or cleanup work to the original feature

Classify roots by the operation that created them. A successful independent-task creation and an explicit subagent spawn are different topology evidence. Do not use a generic `thread_source` value alone; it may be an implementation detail shared by both.

Classify AGY as an implementation executor inside its owning Codex worker, not as
a Codex task root. Record AGY invocations and remediation passes separately when
available; do not combine AGY-reported usage with Codex token totals unless the
measurement source and units are equivalent.

For an AGY-enabled outcome, also record the declared economic hard cap, observed
loops by category, early-stop reason, and the user's stated cost rationale when
available. A higher hard cap can be rational when the external executor is less
expensive, but it does not establish lower total workflow cost. Compare AGY and
Codex prices only with an explicit common currency, equivalent token definitions,
and the observation-date pricing; otherwise publish the counters side by side.
Use the delegation receipt's per-invocation `usage_delta` for loop accounting.
Preserve AGY's `usage_cumulative` as conversation evidence, but do not count the
cumulative value again on each remediation. A cache hit or approval rejection
before AGY starts is not an AGY loop and contributes no invocation usage record.

Report completed outcomes separately from accepted outcomes. A `needs_followup` result can be a completed bounded review without being accepted delivery evidence.

## Context-loading profile

When per-call telemetry is retained, record by workflow component:

- input, cached input, uncached input, and cache ratio
- token-counter increments as a proxy for model/tool cycles, explicitly labeled as a proxy
- median and maximum last-call input
- maximum observed context-window utilization
- compaction count and the phase in which compaction occurred
- automatic-review share of uncached input

Do not describe cumulative input as unique content loaded. Cached input can represent a repeated prompt, instruction, tool, or conversation prefix. Uncached input is cache-missed input, not a semantic count of new information.
Likewise, a high cached-input ratio does not make repeated coordinator or worker
cycles free. Treat full-history inheritance, repeated broad reads, and long
lifecycle reuse as workload-shape signals rather than causal proof.

If raw per-call telemetry is missing for any included task, keep aggregate counters when they can be derived from the frozen snapshot, but report call count, median, maximum, and compaction as `unavailable` for the incomplete group. Do not extrapolate from retained tasks.

If one or more root session logs are missing and no authoritative frozen aggregate
can reconstruct them, report retained telemetry as a **lower bound**, name the
missing component count, and mark the complete total unavailable. Do not present
the retained sum as the workflow total.

Do not claim control over prompt caching, `reasoning.context`, or compaction
thresholds. Measure observed behavior and the workflow controls that are actually
available: packet contents, references loaded, reruns, and bounded cycles.

## Pilot 3 observational validation

Pre-register Pilot 3 as an observational validation of context-loading controls,
not a direct efficiency comparison with Pilot 1 or Pilot 2. Freeze the delivery
cutoff before any separately authorized Ops work and record:

- compact dispatch and acceptance packet presence, field completeness, and size
  using one declared unit such as lines, words, or tokens
- context budget gate and review readiness gate pass/fail decisions
- declared versus observed model/tool cycles, or labeled action-loop proxies
- repeated full-history reads, full-Issue loads, full-diff loads, broad test reruns,
  and full-artifact loads, with a reason for every exception
- coordinator, worker, reviewer, automatic-review, and Ops topology separately
- maximum call input, context utilization, compactions, cached and uncached input,
  and cycle proxies when telemetry is retained
- acceptance result, missing-evidence follow-ups, escaped defects, rework, and any
  required check omitted or delayed by reduction
- whether delivery acceptance stopped cleanly or transitioned to an explicitly
  authorized separately tracked Ops outcome with a declared topology, packet, and cutoff

Report gate adherence and evidence quality even when token telemetry is unavailable.
Compare Pilot 3 numerically with an earlier pilot only if outcome, scope, gates,
model/effort, environment, topology, and cutoff are sufficiently equivalent;
otherwise report workload-shape observations without savings percentages.

## Interpretation

- Higher reasoning effort can increase token use and response time, but one session does not establish a causal benchmark.
- Long context, repeated inspection, tool waits, verification, implementation scope, and rework can also dominate elapsed time.
- Additional workers may reduce wall-clock duration while increasing aggregate tokens.
- A lower cumulative input total can come from fewer model/tool cycles even when median context per cycle changes little.
- Compare equivalent outcomes and gates. Do not compare a partial worker with a complete end-to-end delivery.

## Pilot comparison

Record the serial baseline, coordinator run, worker runs, integration run, environment/date, outcome equivalence, and limitations. Report observations separately from causal claims.
