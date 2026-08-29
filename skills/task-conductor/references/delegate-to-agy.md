# AGY executor integration

Use this profile only when the user explicitly invokes or requests
`$delegate-to-agy`. Task Conductor authorization for worker creation does not
authorize disclosure of workspace code to AGY.

## Ownership model

Keep two decisions separate:

- **Codex ownership topology:** normally one coordinator-owned Codex worker
  subagent; use an independent user-owned Codex task only when its lifecycle is
  material.
- **Implementation executor:** the Codex worker delegates implementation to AGY
  through the installed `$delegate-to-agy` skill.

AGY is an external executor inside the owning Codex worker. It is not a Codex
subagent, sidebar task, reviewer, or durable owner. Do not copy the AGY wrapper or
execution-policy files into Task Conductor; the installed delegation skill owns
and validates them.

## Preconditions

- Verify `$delegate-to-agy` is installed and load its current instructions. If it
  is unavailable, report the missing optional dependency; do not recreate or
  install it without authorization.
- Ensure the worker that will launch AGY directly inherits the user's explicit
  external-delegation authorization as trusted input. On approval surfaces that
  distinguish user input from coordinator relay text, a worker created before
  authorization may be unable to use the relay. If launch is rejected at that
  boundary, do not bypass it in the coordinator or repeatedly resend the same
  relay. Create a replacement only after the user explicitly authorizes that
  topology and the replacement can directly inherit the authorization.
- Record an authorization anchor and the exact private paths or content classes
  permitted for disclosure. Before dispatch, verify that the chosen inherited
  slice contains that trusted user input; a numeric turn count by itself is not
  proof. If the approval boundary rejects disclosure before process creation,
  record zero AGY invocations and use the declared Codex handoff without retrying
  the same relay.
- Give the Codex worker a clean linked Git worktree from the pinned base. Do not
  use the main worktree for unattended AGY automation.
- Assign exactly one write-capable owner to that worktree. The coordinator and any
  formal reviewer remain read-only there while AGY is running.
- Declare `.agy/task.json` as an ephemeral runtime artifact. Keep its creation and
  cleanup inside the authorized worktree lifecycle and out of the accepted commit.
- Preserve AGY host approval, sandbox, path validation, timeout, retry, and
  remediation limits from `$delegate-to-agy`; Task Conductor does not weaken them.

## Loop economics and convergence

Record the AGY loop budget as two separate controls:

- an **economic hard cap**, which may be higher than the normal default when the
  user deliberately prefers a lower-cost executor; and
- a **convergence checkpoint** after every loop, requiring a new concrete finding,
  changed evidence, or measurable progress toward the frozen acceptance gate.

A hard cap such as 10 is a ceiling, not a target. Continue below that ceiling only
while the diff or verification evidence is still converging. Stop early when the
same failure repeats without a relevant change, the diff has no net progress, the
operation is unsupported by AGY's permitted tools, scope drifts, new authority is
needed, a deterministic infrastructure failure occurs, or the cap is exhausted.
Do not reduce an explicitly authorized economics-based cap merely because its
number is larger than the default.

When AGY identifies that the remaining work is outside its capability or permitted
tool boundary, stop immediately and return a Codex handoff packet. Include the
immutable or recorded baseline, actual diff, completed acceptance criteria,
remaining gap, failed or unavailable operation, validation evidence, receipt and
private routing location, and the smallest next Codex action. This is a normal
executor handoff within the owning worker, not permission to widen scope. Codex may
finish only work already inside the worker's authorization and must independently
review the combined result.

Count initial implementation, product remediation, verification-only remediation,
transient infrastructure retry, and Codex catch-up separately. AGY and Codex usage
must remain separate unless their measurement units and prices are demonstrably
equivalent.

## Compact AGY delegation packet

Add these fields to the normal worker packet:

- explicit instruction to use `$delegate-to-agy`
- objective and acceptance criteria
- canonical linked-worktree root
- exact relative read paths, write paths, and out-of-scope paths
- expected final output shape, including every file or directory that a valid
  structural result must create, move, or replace
- relevant existing changes and repository instructions
- focused checks and frozen candidate gate
- AGY implementation and remediation cycle budget
- economic rationale, hard cap, and per-loop convergence checkpoint
- stop conditions for scope drift, non-`SUCCESS`, credentials, new authority, or
  exhausted remediation
- private location for the AGY conversation ID and terminal evidence
- runtime-artifact ownership for environments, dependency trees, caches, generated
  outputs, and the exact cleanup envelope when one is authorized
- objective-specific semantic probes that distinguish a meaningful result from a
  no-op or merely syntactic `SUCCESS`
- capability-handoff contract and the evidence AGY must leave for Codex
- handoff category: `runtime_materialized`, `runtime_only_finding`,
  `unsupported_operation`, `external_disclosure_denied`, or another concise
  evidence-backed category

Do not embed secrets, environment values, unrelated repository content, or the
coordinator's full history.

Preflight the AGY task with the wrapper's validation-only mode and preflight the
declared validation command and runtime requirements before AGY starts. Include
the final intended module directories in the initial write paths; a successful
receipt does not authorize later path expansion.

When practical, use this order: AGY implementation, diff and objective-specific
semantic review, evidence-driven AGY remediation, runtime dependency
materialization, focused checks, then the single owned broad gate. Large ignored
runtime trees can make a later wrapper remediation fail its clean-baseline safety
check. If tests require those trees before remediation, declare that constraint
and the Codex capability-handoff path in advance. Do not delete or rebuild an
environment merely to regain wrapper eligibility. When the user authorizes a
bounded cleanup envelope, validate exact paths and reparse-point boundaries before
using it.

If the requested change requires a structural operation AGY cannot perform under
its permitted tools, such as deleting a tracked file, stop that AGY loop and route
the exact operation back to Codex under the existing authorization boundary. Do
not consume repeated AGY loops producing empty placeholder files or equivalent
non-solutions.

## Evidence and acceptance

The Codex worker must capture the baseline, invoke AGY, inspect actual changes,
run relevant checks, and perform the independent review required by
`$delegate-to-agy`. AGY's response and `SUCCESS` status are execution evidence,
not Task Conductor acceptance evidence.

Immediately after each `SUCCESS`, run the declared objective-specific probe before
expensive broad validation. When the baseline did not already satisfy the
Definition of Done, an unexplained no-op diff, missing target directory, increased
monolith size in a decomposition task, unchanged required metric, or failed
value-equivalence check is a concrete remediation finding even when the receipt is
valid. Count pre-process validation rejection separately; it is not an AGY loop.

The worker completion record must distinguish AGY claims from Codex-verified
results and include AGY version, terminal status, remediation count, changed-file
attribution, validation, and unresolved risks. Keep the conversation ID in a
private routing record when the durable tracker is public.

Keep the successful receipt and private routing record until the immutable
candidate exists and the frozen candidate gate has passed. Removing them after
focused checks can make a later evidence-driven remediation impossible. Exclude
them from the accepted commit and remove them only at the declared lifecycle
cleanup point.

A successful receipt binds the task and actual workspace output; it does not prove
that the output satisfies semantic or portable-byte acceptance. For exact text
bytes across platforms, prefer repository-owned EOL policy and verify the
immutable committed blob. Treat mutable worktree EOL as the acceptance boundary
only when the contract intentionally requires host-specific materialization.

After the worker produces an immutable candidate and the candidate gate passes,
the coordinator may accept it directly when repository policy permits. Use a
separate Codex reviewer only when the declared acceptance policy or risk warrants
another actor; do not repeat a broad gate solely because AGY was the executor.
