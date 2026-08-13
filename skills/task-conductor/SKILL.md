---
name: task-conductor
description: Coordinate or adopt tracked delivery across independent Codex tasks with bounded outcomes, explicit dependencies, isolated branches and worktrees, durable handoffs, controlled concurrency, execution-profile accounting, and evidence-based acceptance. Use when the user explicitly asks for a coordinator task, cross-task orchestration, multiple independent Codex tasks, a controlled parallel pilot, or repository adoption of this workflow. Do not use for ordinary single-task implementation or as implicit authorization to create tasks, trackers, pull requests, deployments, or subagents.
---

# Task Conductor

Coordinate a tracked initiative without making one long task the only source of truth. Keep the coordinator focused on dependencies and acceptance. Give each worker one bounded outcome.

## Required references

Before dispatching work, read:

- applicable repository instructions and task-governance documents
- [`references/git-isolation.md`](references/git-isolation.md)
- [`references/parallel-readiness.md`](references/parallel-readiness.md)
- [`references/status-contract.md`](references/status-contract.md)
- [`references/task-prompts.md`](references/task-prompts.md)
- [`references/context-loading.md`](references/context-loading.md)

Read [`references/measurement.md`](references/measurement.md) when evaluating token use, elapsed time, or a pilot.
Read [`references/troubleshooting.md`](references/troubleshooting.md) when destination resolution, task inventory, ownership checks, creation, or topology verification fails.

## Repository adoption

- Treat global `AGENTS.md` guidance as optional personal configuration, not an installation requirement.
- Prefer repository-local instructions for shared tracker, verification, Git lifecycle, language, and owner-only rules.
- When the user asks to establish governance and none exists, copy and tailor `assets/task-governance-template.md` into the repository's declared documentation location.
- Do not treat the bundled template as active policy until the repository adopts it.
- Do not copy organization-specific rules from another repository without review.

## 1. Confirm preconditions

- Confirm the initiative has a repository-declared durable tracker or another explicitly authorized durable handoff location.
- If neither exists, report the governance gap. Do not invent a tracker or silently make chat the durable record.
- Confirm the user explicitly authorizes creating independent tasks in the current request. This skill does not supply that authorization.
- Confirm task creation, naming, monitoring, and isolation capabilities before promising orchestration.
- Resolve a destination by canonical repository path, host, and repository type. If more than one saved project remains plausible, stop for explicit selection.
- Keep capability, destination-resolution, inventory, ownership, and creation failures separate. One failure is not evidence that another check passed or failed.
- Treat independent tasks and background subagents as different topologies. Authorization for one does not authorize the other.
- If independent task creation fails or returns an unusable destination, stop and report the exact failure. Do not silently substitute a subagent, nested agent, local implementation, or manual background process.
- Keep the first pilot to one worker. Expand concurrency only after one complete dispatch, handoff, and independent acceptance cycle succeeds.
- Do not create a coordinator for one outcome that one task can finish and verify directly.

## 2. Build the task graph

Split only at independently verifiable outcomes. Record for each outcome:

- durable tracker and owner
- dependencies and blockers
- exact in-scope and out-of-scope work
- Definition of Done and required evidence
- branch, worktree, and mutable-resource ownership
- execution profile
- integration order
- authorization boundaries
- one next action

Keep product specification, lifecycle dashboard, and detailed evidence separate
when the tracker supports it. Do not turn one specification file into an
ever-growing execution transcript. Link stable scope to a compact current-state
record and store verbose logs or artifacts at stable evidence locations.

When work crosses a material risk or product boundary, close or pause the current
outcome and create a newly scoped outcome. Publication, infrastructure changes,
credential work, password-policy changes, deployment, and cleanup are not implicit
continuations of a feature outcome merely because they use the same repository.

Use `references/status-contract.md`. Treat task IDs and the live dashboard as routing data, not durable lifecycle state.

## 3. Name tasks and resolve execution profiles

- Title every coordinator, worker, reviewer, and follow-up task as `[project/module] | [bounded outcome] | [role]`.
- Use exactly one independently verifiable outcome in the middle segment. Keep status, dates, sequence-only labels, and task IDs out of titles.
- Pass the title through task creation. Rename immediately when creation-time titles are unavailable.
- Record `default/inherited`, or the explicitly selected model, reasoning effort, and rationale.
- Omit model and reasoning overrides by default. Set a model only when the user explicitly requests that model.
- Pass requested overrides through task-creation fields, not prompt prose alone, and verify destination support before dispatch.
- Treat higher effort and additional workers as separate token and latency decisions.

## 4. Isolate mutating work

- Give every mutating worker a dedicated branch and physical worktree from a pinned base.
- Never assign two mutating tasks to the same branch or worktree.
- Keep the coordinator out of worker implementation scope.
- If dedicated worktrees are unavailable, run mutating outcomes serially in an exclusive checkout or report the limitation. Do not claim safe parallel mutation.
- Follow `references/git-isolation.md` for dispatch, acceptance, integration, and cleanup.

## 5. Apply the parallel readiness gate

- Keep one mutating worker as the default.
- Limit the first parallel pilot to two mutating workers.
- Require explicit current authorization for the exact concurrency and every check in `references/parallel-readiness.md` to pass.
- Stop parallel dispatch when dependency, contract, file/object, resource, or authorization overlap appears.
- Accept workers individually, then run the declared integration acceptance gate.

## 6. Dispatch bounded tasks

- Prefer a clean independent task over forking a long coordinator history.
- Apply the context budget gate and send the compact dispatch packet in `references/context-loading.md`. Do not copy full prior-task histories.
- Declare a model/tool cycle budget and stop condition for every worker and reviewer. A budget limits loops; it does not override required verification.
- When explicitly authorized, declare a correction envelope with exact mutable
  files or components, permitted evidence-driven correction loops, and the single
  broad-gate allowance. Corrections inside that envelope do not need artificial
  per-line follow-up outcomes. Scope, risk-boundary, credential, deployment, and
  destructive changes still require new authorization.
- On every dispatch, verify the invoked creation operation and result identify an independent user-owned task, then retain its task ID as transient routing data. Do not assume topology from an earlier dispatch or infer it from a generic `thread_source` label alone.
- Treat a client-side or pending creation handle as evidence that the creation request was accepted, not that setup is still running or complete. Do not submit the request again. Record the state as `creation accepted / formal ID unresolved / execution unknown` until the formal task ID is correlated.
- Resolve the formal task ID with a supported mapping or status capability when available. A missing recent-inventory entry alone does not prove that setup is pending or that execution has not started.
- Respect the active task-inventory tool's accepted bounds. Treat a rejected or truncated inventory as unknown ownership, then combine recent inventory with known task-ID checks, Git worktree/branch state, and the durable tracker.
- Require the worker to inspect current durable state before editing and to return the worker completion contract.
- Do not allow nested tasks or subagents unless the user explicitly authorizes that topology.
- Use and tailor the templates in `references/task-prompts.md`.

## 7. Monitor with bounded waits

- Prefer cursor-based bounded waits or snapshots. Do not repeatedly reread full task histories.
- For concurrent workers, wait on all active task IDs in one bounded snapshot when supported.
- Notify the user only for meaningful state changes, decisions, failed acceptance, or completion.
- Keep independent workers running when an unrelated worker fails. Stop the batch when shared contract, base, resource, or authorization state drifts.
- Use a follow-up only when outcome and Definition of Done remain unchanged. Track material scope changes as new outcomes.

## 8. Accept evidence, not summaries

Apply the review readiness gate before spending an independent review cycle. Give the reviewer a compact acceptance packet rather than worker history or raw logs.

Require an immutable commit, content-addressed tree, or explicitly recorded stable
diff hash before formal acceptance review. A pre-commit inspection may identify
findings, but it is not the formal acceptance target and must not be followed by a
second broad review merely to discover that the target was mutable.

Independently verify:

- expected repository, branch, worktree, and final HEAD
- pinned-base ancestry, scoped diff, and clean worktree
- required tests and repository verification gates
- durable tracker Definition of Done
- unresolved review, conflict, security, deployment, or owner-only boundaries

Mark an outcome accepted only when evidence is sufficient. Worker confidence is not evidence.

## 9. Stop and hand off

Stop when the initiative is complete, a dependency requires user authority, or remaining work cannot be safely split. Write accepted and blocked outcomes, evidence, execution profiles, decisions, and one next action to the durable tracker. Do not create a competing coordinator backlog.

After delivery acceptance, apply the delivery-to-Ops boundary in `references/context-loading.md`. Continue only for an already authorized bounded handoff; otherwise propose a separately authorized independent Ops task with its own packet and measurement cutoff.

Record token and elapsed-time telemetry when available, but do not invent missing values or claim causation from one observation.
