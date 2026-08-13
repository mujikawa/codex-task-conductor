# Git isolation contract

Use one mutating task per branch and physical worktree.

## Before dispatch

1. Resolve the repository and pinned base commit.
2. Confirm the intended branch and worktree are not owned by another active mutating task.
3. Create or provision a dedicated worktree for the outcome.
4. Record repository, base commit, branch, worktree, and expected remote state.
5. Confirm the worker may perform only the authorized Git lifecycle actions.

Read-only reviewers may use a pinned snapshot without creating a branch. A dedicated worktree is still preferable when local commands can create files or alter indexes.

## Worker rules

- Do not switch to or modify another task's branch or worktree.
- Stop when the pinned base, expected remote head, or ownership state drifts materially.
- Keep unrelated user changes out of the task diff.
- Report the final HEAD, changed files, exact checks, and worktree status.
- Do not push, merge, rebase, force-update, or delete branches unless separately authorized.

## Acceptance and integration

Verify repository identity, base ancestry, final HEAD, scoped diff, clean status, and required checks before acceptance. Define merge order and a conflict owner before combining outcomes. Run the shared verification gate on the integrated state; individual worker success is insufficient.

## Cleanup

Retain the branch and worktree until the result is accepted and every required commit is safely preserved. Remove them only when repository policy and user authorization allow it. Never delete an unmerged or unpreserved branch merely because a task ended.

Classify each accepted worktree promptly as:

- `retain-for-rollback`: required until a named release or rollback boundary
- `cleanup-ready`: merged or otherwise preserved, clean, and no longer needed
- `dirty-owner-action`: contains unpreserved work and must not be removed

Record the expected cleanup point instead of deferring all worktree and branch
inventory to the end of a long initiative. Cleanup remains a separately authorized
destructive lifecycle action.

## Capability fallback

If the platform cannot create dedicated worktrees, keep mutating work serial in an exclusive checkout. Parallel read-only analysis may continue when it cannot modify repository or shared-resource state.
