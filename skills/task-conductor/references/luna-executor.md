# Optional Luna executor

Use only when the user explicitly enables a Luna implementation executor under
the owning Codex worker. Default execution remains `Codex direct`: the worker
implements and verifies its own bounded outcome. Installing this skill or choosing
a worker model does not enable Luna. AGY remains a separate explicit choice.

## Ownership and dispatch

- Keep the coordinator, outcome owner, and executor distinct. The coordinator
  dispatches the worker; the worker may create one Luna subagent for the authorized
  outcome. Luna does not create further agents or delegate to AGY.
- Reuse the user's scoped authorization across implementation and correction
  follow-ups. Record the authorization anchor, worker and child routing IDs, and
  parent lineage. A standalone Luna worker is not this executor topology.
- Resolve the executor's profile using the role table in `../SKILL.md`
  (`gpt-6-luna` / `xhigh` unless overridden). Pass model and effort through supported
  creation fields. With a surface that cannot override a full-history fork,
  choose no history or the smallest trusted slice that preserves required user
  authority; never silently inherit Sol while calling the executor Luna.
- Check nested-agent support and the shared agent-slot limit before dispatch.
  Count the executor as a Codex descendant, within the already authorized
  concurrency limit. If no slot is available, wait for authorized capacity or
  report the limitation; do not increase concurrency or switch topology.
- Assign the outcome's dedicated branch/worktree and exact write paths. Transfer
  its exclusive write ownership to Luna while it runs; the owning worker and
  coordinator remain read-only there. The worker may resume writing only after
  Luna has stopped and the handoff state has been verified. Do not run Luna and
  AGY against the same outcome concurrently.

## Compact executor packet

Use the normal compact dispatch packet and include:

- owning worker, outcome and durable tracker anchor
- canonical worktree, branch, pinned base and current baseline
- exact allowed read/write scope and out-of-scope work
- implementation requirements, Definition of Done and focused checks
- resolved model/effort, selection source and trusted authorization anchor
- runtime-resource ownership, validation owner and frozen candidate gate
- any explicit hard limits, progress-based stop conditions and handoff evidence
- no further delegation, publication or independent acceptance authority

Keep coordinator history and raw logs out of the packet. The worker handles
ambiguous requirements before dispatch instead of asking Luna to widen scope.

## Review, correction and handoff

Luna returns the actual diff or immutable target, changed paths, checks with exact
results, remaining gaps and telemetry when available. The owning worker checks
scope, semantics and evidence independently; executor confidence does not prove
acceptance. Preserve the single broad-gate owner and avoid duplicate gate runs.

For an in-scope finding, send a focused correction to the same executor while
progress continues. Apply the existing completion, progress and authorization
rules; do not invent a retry count. If Luna cannot make useful progress, stop it
and record the baseline, current diff, checks, unresolved gap and smallest next
action. The worker may take over only within already authorized scope and after
exclusive write ownership returns. Preserve the outcome and Definition of Done.
Switching to AGY still requires explicit external-delegation authorization.

Record Luna's profile, routing, correction work and any worker catch-up separately
from the owner. Include its usage once in linked Codex descendant totals; do not
count the owning worker's reported aggregate and the same child tokens twice.
Only the owning worker returns the outcome completion contract to the coordinator.
