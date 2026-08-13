# Status and acceptance contract

## Coordinator dashboard

Use one row per outcome:

| Outcome | Durable tracker | Depends on | Task title / ID | Execution profile | Branch / worktree | Status | Next action |
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

Keep the durable record layered when possible:

- stable specification and Definition of Done
- compact current-state dashboard
- decision log for contract-changing choices
- evidence index pointing to full logs and artifacts

Do not copy every commentary update, command transcript, or authorization exchange
into the stable specification. Preserve only decision-relevant history.

## Worker completion contract

Return:

1. outcome and durable tracker
2. task title and immutable task ID
3. model and reasoning effort, or `default/inherited`
4. repository, branch, worktree, base, and final HEAD
5. changed files and rationale
6. commands and exact pass/fail results
7. Definition of Done evidence
8. unresolved risks, blockers, and owner-only actions
9. token and elapsed-time telemetry when available
10. one recommended next action

If incomplete, update the durable handoff instead of leaving state only in chat.

Before review, reduce this record to the compact acceptance packet in
`context-loading.md`. Keep full logs and artifacts at stable evidence locations.

## Coordinator acceptance record

Record acceptance time, accepted HEAD or review target, independently verified checks, satisfied Definition of Done items, parallel and integration evidence when applicable, deferred scope, telemetry availability, and one next action.

Acceptance verifies evidence. It does not authorize deployment, destructive actions, merge bypasses, or other owner-only operations.

After acceptance, record whether the next action remains an authorized bounded
handoff or requires a proposed independent Ops task. A proposed Ops task needs new
authorization, its own dispatch packet, and a separate measurement boundary.
