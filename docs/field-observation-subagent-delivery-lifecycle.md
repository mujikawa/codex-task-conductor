# Subagent delivery-lifecycle field observation

## Scope

This anonymized observation covers one explicitly authorized vertical-slice
delivery from durable rollover adoption through implementation, independent
review, GitHub publication, reconciliation, and cleanup. It is workflow evidence,
not a controlled efficiency benchmark. Private repository, host, task, commit,
issue, pull-request, and path identifiers are intentionally omitted.

## Observed topology and result

- One independent user-owned coordinator adopted a durable product checkpoint.
- Seven coordinator-owned Codex subagents ran with no inherited conversation
  history: foundation, two non-overlapping feature workers, integration, first
  reviewer, bounded review correction, and second reviewer.
- The foundation pilot ran alone. The two feature workers ran concurrently only
  after the foundation target was accepted and file, contract, generated-output,
  and runtime ownership passed the parallel-readiness gate. Peak mutating
  concurrency was two despite an authorized ceiling of three.
- Every mutating worker used a dedicated branch and linked worktree. The
  integration worker was the sole writer for shared routing, generated contracts,
  CSS entrypoints, and browser-smoke ownership.
- The first independent reviewer returned `needs_followup` with three actionable
  findings. The coordinator stopped after the original correction envelope was
  exhausted and resumed only after a new, finding-specific envelope was
  authorized.
- The corrected immutable target passed the repository quick and delivery gates,
  then the second independent reviewer returned `accept` with no actionable
  findings.
- Publication used one product pull request followed by two tracker-only pull
  requests. All three CI runs passed and all three pull requests merged. The
  product outcome was accepted and published; cleanup retained one preserved
  integration ref and empty host-held directories for a later safe retry.

## Measurement boundary

The implementation-and-lifecycle boundary began at explicit delivery
authorization and ended at the final merged lifecycle report, about three hours
and forty-nine minutes later. The broader coordinator session, including earlier
scope adjudication, spanned about four hours and thirty-eight minutes.

The frozen delivery cutoff included the coordinator, seven worker or reviewer
subagents, and two related automatic approval-review roots. All ten retained root
logs reported token counters:

| Component | Roots | Input | Cached input | Output | Reasoning output | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Coordinator | 1 | 56,107,136 | 55,241,472 | 179,351 | 66,794 | 56,286,487 |
| Workers and reviewers | 7 | 51,149,419 | 49,770,496 | 266,493 | 87,321 | 51,415,912 |
| Automatic approval review | 2 | 11,621,278 | 11,088,128 | 9,465 | 2,973 | 11,630,743 |
| Aggregate | 10 | 118,877,833 | 116,100,096 | 455,309 | 157,088 | 119,333,142 |

Cached input was about 97.7% of reported input; uncached input was 2,777,737.
These are cumulative processing counters, not unique semantic content. The
observation does not attribute the total to one model, topology, or workflow
choice.

The coordinator log recorded 131 bounded agent waits and two compactions. Active
model time versus tool, test, CI, and approval wait time was unavailable.

## What worked

1. The single-worker foundation pilot exposed contract defects before parallel
   mutation began. Frozen-base feature work then achieved useful concurrency
   without shared-file conflicts.
2. Compact packets with no inherited history were sufficient for all seven
   subagents because scope, authorization anchors, ownership, validation, and stop
   conditions were explicit and durable state was authoritative.
3. Coordinator acceptance found migration ordering, recipient-domain validation,
   and notification-content gaps after the foundation worker reported success.
   Immutable commits, manifests, focused reruns, and semantic inspection prevented
   worker confidence from becoming acceptance evidence.
4. The first reviewer found boundary rounding, least-privilege navigation, and
   state-recovery defects after the broad suites passed. This validated a
   read-only semantic reviewer that targets risks not represented by aggregate
   test counts.
5. The exhausted correction envelope caused a real stop. A new owner-authorized
   envelope constrained remediation to the three findings and their adjacent test
   contracts instead of silently widening delivery authority.

## Gaps and resulting controls

1. The integration worker ran the full quick and delivery gates, then the
   coordinator repeated the same broad gates on the unchanged immutable target.
   The workflow now chooses either a worker-owned or coordinator-owned broad gate
   before integration. Independent acceptance verifies semantics and evidence
   without duplicating the same commands merely to add an actor.
2. Fixed one-minute monitoring produced 131 waits and many unchanged status
   cycles. Monitoring now backs off during long tests and CI, resets after a
   material transition, and avoids commentary for unchanged polls.
3. Two tracker-only pull requests followed the product pull request because a
   reconciliation pull request could not record its own future merge identifier.
   The workflow now prefers one post-merge tracker pull request and records its
   terminal identifier in the pull-request body, comment, or another lifecycle
   receipt instead of opening a recursive finalization pull request.
4. Delivery, publication, reconciliation, and cleanup were described too closely
   as one completion state. The workflow now records separate lifecycle facets;
   an accepted and merged product may remain
   `cleanup-pending-host-release` without being reopened or force-cleaned.
5. Canonical subagent routing names could not carry the human-readable worker
   title format. The workflow now treats constrained agent paths as routing data
   and preserves the display title in the dispatch packet and durable tracker.

## Interpretation

The observation supports a subagent-first topology with a serial contract pilot,
controlled two-worker concurrency, one integration writer, and independent
semantic review. It does not establish token or elapsed-time savings. The useful
result is a stricter ownership shape and four concrete cost controls: one broad-
gate owner, adaptive monitoring, finite reconciliation, and honest cleanup state.
