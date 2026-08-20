# Dispatch troubleshooting

Use this guide when worker preflight or dispatch fails. Preserve the requested topology and authorization boundary while diagnosing it. The independent-task sections apply only when that topology was selected.

## Contents

- Classify the failure
- Subagent creation or routing fails
- Independent task creation fails
- One repository maps to multiple saved projects
- Task inventory exceeds a runtime bound
- Creation is accepted while the formal ID is unresolved
- Prove ownership with multiple sources
- Prevent silent topology drift
- Host and Windows preflight
- Safe recovery report

## Classify the failure

Report these dimensions separately:

- **Capability:** the required task-management operation is unavailable.
- **Destination:** the repository cannot be mapped to one saved project and host.
- **Inventory:** task listing was rejected, truncated, or otherwise incomplete.
- **Ownership:** available evidence cannot establish exclusive branch, worktree, resource, or outcome ownership.
- **Creation:** the independent-task creation operation failed or returned no usable task ID.
- **Topology:** the result is a subagent or another execution form instead of the authorized independent task.

Do not collapse them into a generic dispatch failure. A failure in one dimension does not prove conflict or clearance in another.

## Subagent creation or routing fails

1. Confirm whether spawning returned an agent ID or path before retrying.
2. Inspect the active agent inventory and parent lineage once.
3. Retry only when the first request definitely created nothing.
4. Stop and report the exact error or unresolved routing state otherwise.
5. Do not create an independent task or implement the worker scope in the coordinator without new explicit authorization.

## Independent task creation fails

1. Confirm whether creation produced a task ID before retrying.
2. Refresh the active project list and task-creation contract once.
3. Retry once only when the destination is unique and the first attempt definitely created nothing.
4. Stop and report the exact error if uncertainty remains.
5. Do not substitute a background subagent, nested agent, coordinator implementation, or manual background process without new explicit authorization.

Task creation failure is a topology blocker, not permission to change topology.

## One repository maps to multiple saved projects

Compare canonical repository path, host, repository type, and label. Do not select by label or stale project ID alone.

If multiple candidates still point to the same canonical destination, report the candidates without publishing private identifiers and request explicit selection or saved-project cleanup. Refresh the project list before a later dispatch; do not assume an earlier identifier remains valid.

Explicit user selection resolves routing ambiguity without deleting the duplicate metadata. Cleanup is not a dispatch prerequisite when all of these conditions pass:

1. refresh the project list immediately before dispatch
2. match the selected project to the expected canonical path, host, and repository type
3. exclude every unselected duplicate from the creation request
4. independently classify task, branch, worktree, tracker, and mutable-resource ownership as `clear`
5. retain explicit current authorization for exactly the intended dispatch

If any mapping drifts, return to destination resolution instead of selecting another duplicate automatically.

## Task inventory exceeds a runtime bound

Read the active tool contract and use a value within its accepted range. In one observed Codex Desktop pilot, a request for 100 recent non-pinned tasks was rejected because that runtime accepted at most 50. Treat 50 as an observation, not a permanent product guarantee.

A validation error means the inventory query did not run. It does not mean:

- an ownership conflict exists
- ownership is clear
- task creation is unavailable
- a background subagent is an acceptable fallback

Retry the read-only inventory query once with a valid bound. Do not perform task creation in the same recovery step unless the user already authorized dispatch and every other precondition is satisfied.

## Creation is accepted while the formal ID is unresolved

Some task-creation surfaces return a client-side or pending creation handle before the coordinator can resolve the formal task ID. The handle proves that the creation request was accepted; it does not by itself prove whether worktree setup is pending, complete, or failed.

Use this three-part state until stronger evidence is available:

- creation: `accepted`
- formal task ID: `unresolved`
- execution: `unknown`

Then:

- do not retry task creation or substitute a subagent
- do not pass the client-side handle to operations that require a formal task ID
- retain the handle, creation timestamp, destination, requested title, and expected repository as correlation evidence
- prefer a supported handle-to-task mapping or setup-status capability when available
- take only bounded inventory snapshots and correlate candidates by title, host, repository, creation time, branch, and worktree
- if the UI exposes a formal task ID, ask the user for it and verify its metadata before monitoring
- begin formal monitoring only after the task ID and host are known
- report `formal ID unresolved; execution unknown` when correlation remains unavailable

A task can exist and begin execution before recent-task inventory exposes its formal ID. Inventory absence is therefore a visibility limitation, not proof that setup is still running or that the worker has not started. Report a setup failure only when a setup-status result or equivalent direct evidence says provisioning failed.

## Prove ownership with multiple sources

A bounded recent-task list may omit older non-pinned tasks. Absence from that list is not complete proof that no owner exists.

Combine available evidence:

1. recent task inventory within the current runtime bound
2. direct status reads for known task IDs
3. repository branch and `git worktree list --porcelain` state
4. the durable tracker's current owner, status, and next action
5. mutable-resource ownership for databases, environments, deployments, or other shared systems

Classify the result as `clear`, `conflict`, or `unknown`. Stop dispatch on `conflict` or `unknown` unless repository policy defines a safe resolution.

## Prevent silent topology drift

For every worker, record the requested topology, creation operation, returned task ID, and observed topology. Re-check these fields on every dispatch.

If a coordinator produces a topology different from the recorded authorization,
stop the batch. Preserve durable handoff state and request explicit authorization
before changing topology or recreating unfinished work. Sidebar placement is not
topology evidence; use the creation operation, routing ID, and lineage.

## Host and Windows preflight

Before dispatching or publishing from Windows:

- canonicalize repository and worktree paths with
  `[System.IO.Path]::GetFullPath()` and compare them with
  `[System.StringComparison]::OrdinalIgnoreCase`
- treat detached HEAD as valid when the packet intentionally pins an immutable
  commit; do not call string methods on a missing branch name
- execute the selected Python or other runtime with a harmless version/import
  probe; file existence alone does not prove that a virtual environment is usable
- list required ignored fixtures separately because worktree creation may not copy
  them from another checkout
- test the currently exposed task, wait, handoff, connector, and CLI operations
  independently; one available surface does not prove another handler or login is
  usable

Keep connector authentication and CLI authentication as separate facts. Prefer a
working purpose-built connector for supported operations, and do not describe an
invalid CLI token as failure of an independently authenticated connector.

## Safe recovery report

Return:

- requested outcome and topology
- failure dimension and exact error
- whether any task was created
- returned formal task ID or client-side creation handle
- destination candidates without secrets or private identifiers in public artifacts
- inventory scope and runtime bound used
- ownership evidence and `clear` / `conflict` / `unknown` result
- one safe next action
