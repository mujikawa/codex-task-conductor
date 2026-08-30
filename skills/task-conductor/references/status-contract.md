# Status and acceptance contract

## Coordinator dashboard

Use one row per outcome:

| Outcome | Durable tracker | Depends on | Topology / routing ID | Executor / execution profile | Branch / worktree | Status | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- |

Allowed statuses:

- `planned`: bounded and ready for authorization or dispatch
- `blocked`: waiting for a named dependency or decision
- `running`: worker owns the outcome
- `needs_followup`: evidence is incomplete or failed
- `integrating`: individual outcomes are accepted and integration acceptance is running
- `accepted`: coordinator verified the complete Definition of Done
- `superseded`: replaced by a newly scoped tracked outcome

The dashboard is transient. The repository-declared tracker is durable.

## Outcome manifest

Keep one durable row per bounded outcome with its outcome ID, worker routing ID,
immutable commit, PR or publication identifier, acceptance state, and Ops state.
Treat missing values as explicit `none` or `unavailable`. Compute summary counts
from these rows and reconcile every reported identifier to exactly one row. Do
not hand-count an inclusive PR range or copy a narrative total that can drift from
the manifest.

Keep the durable record layered when possible:

- stable specification and Definition of Done
- compact current-state dashboard
- decision log for contract-changing choices
- evidence index pointing to full logs and artifacts

Do not copy every commentary update, command transcript, or authorization exchange
into the stable specification. Preserve only decision-relevant history.

For delivered outcomes, record lifecycle facets separately:

| Facet | Example states |
| --- | --- |
| Delivery | `needs_followup`, `accepted` |
| Publication | `not-authorized`, `pending`, `merged` |
| Reconciliation | `not-required`, `pending`, `complete` |
| Cleanup | `not-authorized`, `cleanup-ready`, `cleanup-pending-host-release`, `complete` |

Do not collapse these facets into one `complete` label. When cleanup is blocked by
an active task or host handle, record the exact preserved refs or paths and one
safe next action without changing an accepted delivery back to `needs_followup`.

## Worker completion contract

Return:

1. outcome and durable tracker
2. worker title, topology, and agent path or immutable task ID
3. implementation executor; for AGY, version, terminal status, private conversation-routing location, and remediation count
4. model and reasoning effort, or `default/inherited`
5. repository, branch, worktree, base, and final HEAD
6. changed files and rationale
7. commands and exact pass/fail results
8. Definition of Done evidence
9. unresolved risks, blockers, and owner-only actions
10. token and elapsed-time telemetry when available
11. one recommended next action

If incomplete, update the durable handoff instead of leaving state only in chat.

Before review, reduce this record to the compact acceptance packet in
`context-loading.md`. Keep full logs and artifacts at stable evidence locations.

## Coordinator acceptance record

Record acceptance time, accepted HEAD or review target, independently verified checks, satisfied Definition of Done items, parallel and integration evidence when applicable, deferred scope, telemetry availability, and one next action.

Do not record `accepted` before every frozen single-worker candidate gate passes.
When a required gate depends on merged or combined state, record `integrating`
until it passes. If a required gate fails after an accepted claim, classify it as
an escaped acceptance defect, reopen the outcome, and record the correction,
rereview, and republication evidence separately.

Acceptance verifies evidence. It does not authorize deployment, destructive actions, merge bypasses, or other owner-only operations.

After acceptance, freeze the delivery manifest and measurement cutoff, then record
whether the next action remains an authorized bounded
handoff or requires a separately tracked Ops outcome. The Ops outcome needs new
authorization, an explicit subagent or independent-task topology, its own dispatch
packet, and a separate measurement boundary.
