# AGY executor integration

Use this profile only when the user explicitly requests `$delegate-to-agy`.
Authorization to create a Codex worker does not authorize disclosure to AGY.

## Policy ownership

Load the installed `$delegate-to-agy` skill before dispatch. It is the authority
for AGY invocation modes, trusted disclosure, sandbox and path checks, timeouts,
failure retries, remediation caps, Codex handoff eligibility, and receipt handling.
Do not duplicate or weaken that policy here. If the skill is unavailable, report
the missing dependency rather than inventing an executor.

Task Conductor owns the worker, dependency graph, durable outcome, and acceptance.
AGY is an external implementation executor inside the Codex worker, not a Codex
subagent, independent task, reviewer, or durable owner. Removing default Codex
cycle budgets does not remove AGY's external-executor limits.

## Dispatch and isolation

- Select the already-authorized Codex worker topology and bind it to the repository
  and host. Do not create an extra independent task solely to invoke AGY.
- Preserve trusted user authorization in the worker's inherited context as required
  by `$delegate-to-agy`; a coordinator relay or numeric turn count alone is not
  proof. Record the authorization anchor and permitted disclosure scope.
- Use unattended wrapper execution for automated workers. Give a mutating worker
  a clean linked worktree from the pinned base and exactly one write-capable owner.
  The coordinator and reviewers remain read-only while AGY is running.
- Keep the wrapper and execution policy in the installed delegation skill. Do not
  copy or modify them in the target repository.
- Keep `.agy/task.json` and receipts as private runtime artifacts outside the
  accepted commit. Declare their creation, retention, and authorized cleanup.

## Worker packet

Extend the normal compact packet with:

- instruction to use the installed `$delegate-to-agy` and unattended wrapper
- objective, acceptance criteria, pinned baseline, canonical linked-worktree root
- exact read/write paths, exclusions, and trusted external-disclosure authorization
- required output shape, including every destination that a valid result needs
- objective-specific semantic probes, focused checks, and broad-gate owner
- AGY policy defaults or an explicitly authorized cap override and economic rationale
- runtime dependency requirements, receipt retention, and authorized cleanup scope
- private receipt/conversation-routing location
- whether the user requires AGY-only completion; otherwise preserve the installed
  skill's handoff to Codex for already-authorized work

Preflight the wrapper in validation-only mode and check required validation
commands before AGY starts. Account for operations that its permitted tools cannot
perform and declare the eligible Codex handoff. Do not spend retries attempting
an unsupported structural operation or delete an environment to regain wrapper
eligibility. Follow the installed skill's runtime-materialization guidance.

## Monitoring and handoff

An AGY stop ends that executor's invocation loop. The owning Codex worker inspects
the actual partial output and follows `$delegate-to-agy` to decide whether it may
finish the existing outcome. A host denial never authorizes bypassing the denied
action. An AGY-only requirement or missing Codex authority remains a blocker.

Keep the same outcome and Definition of Done for eligible executor handoffs.
Preserve baseline, actual diff, completed criteria, remaining gap, unavailable
operation, validation evidence, private receipt, and next action. Do not relabel a
failed AGY invocation as `SUCCESS` when Codex subsequently completes the outcome.

Record AGY invocations, infrastructure retries, product remediation, and Codex
completion separately. Pre-process rejection, validation-only runs, and receipt
cache hits are not AGY invocations. Keep external and Codex usage separate; consult
`measurement.md` when cost or elapsed-time analysis is requested.

## Acceptance

The Codex worker independently reviews the actual scoped diff and verifies
objective-specific semantics before expensive broad checks. A valid receipt or
AGY `SUCCESS` is execution evidence, not delivery acceptance. Investigate no-op
diffs and wrong output shapes when the baseline did not already satisfy the goal.

Keep successful receipts and private routing until the immutable candidate and
required gate exist, so an eligible remediation remains possible. For exact-byte
acceptance, follow the repository's EOL policy and inspect the intended immutable
blob rather than assuming host worktree bytes are the portability contract.

Accept only after the normal Task Conductor evidence gate passes. The coordinator
may accept directly when repository policy permits; use an additional reviewer
only when policy or risk warrants it. Do not repeat a passing broad gate merely
because AGY produced the implementation. Keep detailed executor evidence in the
private record and report the outcome, verification, handoff, and blockers briefly.
