# Task governance

This repository uses [tracker name and location] as the canonical queue for unfinished work.

Replace every bracketed field before adopting this document. Remove sections that do not apply.

## When to track work

Create or reuse one tracked outcome when work:

- crosses tasks, sessions, repositories, branches, or worktrees
- has an independently verifiable Definition of Done
- requires a decision, authorization, or handoff
- may remain unfinished after the current working session

Do not create a competing backlog file or leave the only durable state in chat, memory, or a pull-request comment.

## Canonical record

- Tracker: [GitHub Issues, Linear, Jira, or another system]
- Project or repository: [owner]
- Local fallback, if explicitly permitted: [path or `none`]
- Fallback migration rule: [when and how local state moves to the canonical tracker]

Before starting, search for an existing outcome, read its latest state, confirm its owner, and identify one next action.

## Required outcome fields

Keep stable scope in the canonical record:

- outcome and owner
- in-scope and out-of-scope work
- dependencies and blockers
- Definition of Done
- required verification and acceptance evidence
- branch, worktree, and mutable-resource ownership
- environment, cache, port, database, generated-output ownership, and permitted
  create, reuse, rebuild, normalize, and cleanup actions
- authorization boundaries
- one next action

Append progress, evidence, decisions, and handoffs to the tracker's activity history rather than repeatedly rewriting stable scope.

When the tracker is file-based, prefer separate or clearly bounded sections for:

- stable specification and Definition of Done
- current lifecycle dashboard
- decisions that changed the contract
- evidence index linking full logs and artifacts

Do not grow the stable specification by copying routine commentary or raw command
output into it.

## Lifecycle

Use these states, or map the team's existing states to them:

- `planned`: bounded and waiting for authorization or dispatch
- `blocked`: waiting for a named dependency or decision
- `running`: owned by one active worker
- `needs_followup`: acceptance evidence is incomplete or failed
- `integrating`: individual outcomes are accepted and integration verification is running
- `accepted`: the complete Definition of Done has independent evidence
- `superseded`: replaced by a newly scoped tracked outcome

Only one worker owns a bounded outcome at a time. Record ownership changes and the single next action.

## Handoff

A handoff must record:

- current status and owner
- repository, branch, worktree, base, and final HEAD when applicable
- changed scope and relevant files
- commands and exact pass or fail results
- satisfied and unsatisfied Definition of Done items
- blockers, risks, decisions, and owner-only actions
- one next action

Do not treat a confident summary as acceptance evidence.

## Authorization boundaries

A tracker authorizes tracking, not every action needed to complete the work. Require the repository's declared authorization for:

- production deployment or mutation
- destructive database or filesystem operations
- credentials, secrets, permissions, or security settings
- force pushes, bypasses, or deletion of unmerged work
- task creation or concurrency when not already authorized
- [additional owner-only actions]

## Closure

Close or mark an outcome accepted only when:

- every Definition of Done item has evidence
- required worker and integration gates pass
- no required candidate gate was deferred until after an accepted or published claim
- unresolved scope is explicitly deferred to another tracked outcome
- the accepted revision or artifact is recorded
- no required handoff or owner action remains

If scope changes materially, create a new tracked outcome instead of silently expanding the existing one.
