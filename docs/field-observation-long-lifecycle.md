# Field observation: long lifecycle expansion

## Status

Retrospective observation recorded on 2026-08-13 from a local Codex Desktop
workflow on Windows. Repository, task, account, host, branch, pull-request, and
production identifiers are intentionally omitted.

This is not Pilot 3, a controlled comparison, or evidence that Task Conductor
caused a token or elapsed-time change. The workflow began as one administration UI
feature and later expanded into publication, production deployment, account
provisioning, transport topology, password policy, and repository cleanup.

## Measurement limits

The coordinator, two retained delivery roots, one inert staging root, one
publication root, and retained automatic-review descendants were available. Two
other independent delivery-worker root logs were no longer present. No
authoritative frozen aggregate could reconstruct those roots.

All token figures below are therefore **retained-session lower bounds**. Complete
workflow totals, active model time, tool/test wait time, and missing-root per-call
profiles are unavailable. Reasoning tokens are included within output/total usage
and are shown only as a diagnostic subset where needed.

The workflow start was `2026-08-12T08:33:03.891Z`.

| Boundary | Elapsed from start | Retained sessions | Missing roots | Retained token lower bound | Increment from prior boundary |
| --- | ---: | ---: | ---: | ---: | ---: |
| Delivery accepted | 7h 27m 45s | 11 | 2 | 90,080,855 | unavailable |
| Publication merged | 8h 13m 47s | 13 | 2 | 109,665,646 | 19,584,791 |
| Initial production delivery accepted | 10h 1m 40s | 13 | 2 | 149,736,822 | 40,071,176 |
| Expanded product/release work complete | 19h 36m 56s | 14 | 2 | 237,721,299 | 87,984,477 |
| Observation cutoff during cleanup | 20h 41m 53s | 14 | 2 | 244,327,301 | 6,606,002 |

At delivery acceptance, retained input was 89,657,647 tokens, including 85,275,904
cached tokens (95.11%). At the observation cutoff, retained input was 243,417,227,
including 231,832,064 cached tokens (95.24%). High cache ratios do not make the
repeated cycles free and do not turn cumulative input into unique content.

## What worked

- Pinned bases, dedicated worktrees, immutable commits, and tree-identity checks
  preserved reviewable delivery state.
- Independent acceptance found real defects in date boundaries, concurrent
  revision enforcement, executable restore documentation, fail-fast behavior,
  privilege assumptions, health gates, and platform-dependent assertions.
- Backup restore tests, checksums, preflight gates, atomic cutovers, and rollback
  evidence protected production during failed attempts.
- Delivery, publication, merge, and live mutation received explicit authorization
  rather than being inferred from implementation work.

## Cost and rework signals

- The coordinator remained the container for nearly every later lifecycle phase,
  so bounded workers did not keep the overall initiative bounded.
- Several same-scope corrections stopped for one selector, one heading boundary,
  one whitespace line, or one fixture adjustment. The controls prevented silent
  budget expansion but created avoidable authorization and context cycles.
- Formal review sometimes began before an immutable target existed, causing review,
  correction, commit, and verification to repeat.
- A single specification file accumulated product contract, dashboard, decisions,
  execution history, deployment evidence, and cleanup state.
- Production cutovers exposed assertion and health-gate bugs that representative
  same-platform rehearsal could have caught earlier.
- Worktree cleanup was deferred until many accepted worktrees had accumulated,
  increasing disk, ACL, and process-lock cleanup complexity.

## Workflow changes

This observation motivated the following rules:

1. Use an explicit correction envelope for bounded, evidence-driven changes inside
   the same scope; require new authorization when risk or scope changes.
2. Require a commit, content-addressed tree, or recorded stable diff hash before
   formal acceptance review.
3. Separate stable specification, current dashboard, decisions, and detailed
   evidence instead of using one growing document for every concern.
4. Freeze a measurement boundary whenever work expands into a new feature,
   infrastructure, credential, policy, deployment, or cleanup outcome.
5. Add Windows path, detached-HEAD, executable-runtime, ignored-fixture, handler,
   and authentication checks to host preflight.
6. Rehearse production scripts and platform-dependent assertions against
   representative output before live mutation.
7. Classify accepted worktrees promptly as rollback-retained, cleanup-ready, or
   dirty-owner-action.

## Interpretation

The defensible conclusion is that the workflow delivered strong isolation and
failure containment while accumulating high coordination and lifecycle-expansion
cost. The retained telemetry establishes a lower-bound operational observation;
it does not establish how much a different workflow would have cost.
