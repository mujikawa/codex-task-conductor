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
- Give the Codex worker a clean linked Git worktree from the pinned base. Do not
  use the main worktree for unattended AGY automation.
- Assign exactly one write-capable owner to that worktree. The coordinator and any
  formal reviewer remain read-only there while AGY is running.
- Declare `.agy/task.json` as an ephemeral runtime artifact. Keep its creation and
  cleanup inside the authorized worktree lifecycle and out of the accepted commit.
- Preserve AGY host approval, sandbox, path validation, timeout, retry, and
  remediation limits from `$delegate-to-agy`; Task Conductor does not weaken them.

## Compact AGY delegation packet

Add these fields to the normal worker packet:

- explicit instruction to use `$delegate-to-agy`
- objective and acceptance criteria
- canonical linked-worktree root
- exact relative read paths, write paths, and out-of-scope paths
- relevant existing changes and repository instructions
- focused checks and frozen candidate gate
- AGY implementation and remediation cycle budget
- stop conditions for scope drift, non-`SUCCESS`, credentials, new authority, or
  exhausted remediation
- private location for the AGY conversation ID and terminal evidence

Do not embed secrets, environment values, unrelated repository content, or the
coordinator's full history.

## Evidence and acceptance

The Codex worker must capture the baseline, invoke AGY, inspect actual changes,
run relevant checks, and perform the independent review required by
`$delegate-to-agy`. AGY's response and `SUCCESS` status are execution evidence,
not Task Conductor acceptance evidence.

The worker completion record must distinguish AGY claims from Codex-verified
results and include AGY version, terminal status, remediation count, changed-file
attribution, validation, and unresolved risks. Keep the conversation ID in a
private routing record when the durable tracker is public.

A successful receipt binds the task and actual workspace output; it does not prove
that the output satisfies semantic or portable-byte acceptance. For exact text
bytes across platforms, prefer repository-owned EOL policy and verify the
immutable committed blob. Treat mutable worktree EOL as the acceptance boundary
only when the contract intentionally requires host-specific materialization.

After the worker produces an immutable candidate and the candidate gate passes,
the coordinator may accept it directly when repository policy permits. Use a
separate Codex reviewer only when the declared acceptance policy or risk warrants
another actor; do not repeat a broad gate solely because AGY was the executor.
