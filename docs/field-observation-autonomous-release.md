# Autonomous release field observation

## Scope

This anonymized observation covers one explicitly authorized coordinator that
delivered nine dependent frontend outcomes, completed their GitHub lifecycle, and
continued through a rollback-protected production cutover. It is workflow evidence,
not a controlled efficiency benchmark. Private repository, task, host, and raw
routing identifiers are intentionally omitted.

## Observed topology and result

- Nine coordinator-owned Codex workers each owned one linked worktree and one
  immutable outcome commit.
- Workers ran serially because later accessibility adoption and decomposition
  outcomes depended on earlier shared contracts.
- Seven workers managed AGY implementations. Twelve real AGY implementation or
  remediation invocations reported success; two later outcomes used Codex direct
  after a private-source approval boundary stopped external delegation before
  process creation.
- The coordinator accepted and published nine outcomes, reconciled the branches
  and worktrees, ran integrated verification, and deployed the accepted release.
- The first activation rolled back safely because the health probe ran before the
  service was ready. A bounded readiness loop allowed the second activation to
  pass without changing the accepted product scope.

## Measurement shape

The complete implementation, publication, and deployment turn took about three
hours and twenty-four minutes. Worker intervals summed to about seventy-three
minutes; the remaining wall time included coordinator acceptance, CI, publication,
deployment, recovery, and live verification and is not active-model time.

Codex logs showed a high cached-input ratio, but cumulative input remained large.
The coordinator accounted for most cumulative input, workers returned compact
bounded evidence, and automatic approval review contributed a material share of
uncached input. AGY reported per-invocation token and duration deltas separately;
those counters were not added to Codex totals because the accounting definitions
were not equivalent.

## What worked

- Compact three-turn inheritance was sufficient for all nine workers to execute
  their bounded outcomes, while dedicated worktrees prevented mutation overlap.
- Objective-specific probes found material issues after several AGY `SUCCESS`
  responses and routed concrete findings back to the same conversations.
- When runtime materialization made further AGY remediation ineligible, bounded
  Codex capability handoffs completed only the already-authorized scope.
- A private-source disclosure rejection produced zero AGY invocations and no
  bypass. Codex direct execution preserved progress.
- Rollback, backup verification, immutable release identification, and live
  browser checks turned deployment recovery into evidence rather than an
  unbounded product correction loop.

## Gaps and resulting controls

1. A fixed inherited-turn count did not prove that every later worker could show
   the exact trusted external-disclosure authorization. Dispatch now records and
   verifies an authorization anchor and disclosed path classes.
2. The completion narrative misstated the number of PRs even though the identifiers
   and worker count showed nine. Summary counts now derive from a reconciled
   outcome manifest.
3. Delivery, publication, and production Ops shared one long coordinator turn,
   obscuring phase cost and increasing compaction pressure. The workflow now
   freezes a delivery cutoff before Ops and prefers rollover for material live work.
4. Coordinator review and CI were sufficient for each bounded outcome, but a
   multi-outcome production release can justify one final read-only integrated
   reviewer. This is a risk decision, not a default reviewer per worker.
5. The successful readiness fix lived in an ephemeral deployment script. A live
   recovery improvement should be promoted into durable deployment tooling or a
   runbook under a separately tracked Ops outcome.

## Interpretation

The observation supports autonomous splitting and bounded external delegation.
It does not establish token savings: publication, approval review, coordinator
cycles, and production validation remained substantial. The useful result is a
more auditable control shape—small workers, explicit handoffs, reconciled outcome
counts, and a measurable delivery-to-Ops boundary.
