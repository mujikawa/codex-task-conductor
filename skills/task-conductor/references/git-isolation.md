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

Verify repository identity, base ancestry, final HEAD, scoped diff, clean status,
and the frozen repository-wide candidate gate on the immutable target before
formal review or single-worker delivery acceptance. Define merge order and a
conflict owner before combining outcomes. Run the shared verification gate on the
integrated state; individual worker success is insufficient.

When integration is required before a shared gate can run, use `integrating`, not
`accepted`, until the gate passes. If repository policy requires merge before that
gate, keep the outcome open and record the merge as provisional integration. A
later required-gate failure is an escaped acceptance defect, not ordinary evidence
collection.

Prefer a freshly materialized immutable acceptance checkout when a long-lived
worker worktree has unexplained EOL, environment, or generated-output drift. Do not
rewrite a Git-clean delivery checkout merely to make verification tools agree
unless that exact normalization is authorized and content identity is proven.

## Cleanup

Retain the branch and worktree until the result is accepted and every required commit is safely preserved. Remove them only when repository policy and user authorization allow it. Never delete an unmerged or unpreserved branch merely because a task ended.

Classify each accepted worktree promptly as:

- `retain-for-rollback`: required until a named release or rollback boundary
- `cleanup-ready`: merged or otherwise preserved, clean, and no longer needed
- `dirty-owner-action`: contains unpreserved work and must not be removed

Record the expected cleanup point instead of deferring all worktree and branch
inventory to the end of a long initiative. Cleanup remains a separately authorized
destructive lifecycle action.

If a live task, process, or Windows directory handle prevents safe cleanup after
the commits are preserved, classify the facet as
`cleanup-pending-host-release`. Record worktree registration, residual branch
refs, remaining directory contents, and the next safe retry point. Do not use
force-removal, recursive deletion, or a cross-shell workaround merely to make the
cleanup summary look complete.

## Capability fallback

If the platform cannot create dedicated worktrees, keep mutating work serial in an exclusive checkout. Parallel read-only analysis may continue when it cannot modify repository or shared-resource state.
