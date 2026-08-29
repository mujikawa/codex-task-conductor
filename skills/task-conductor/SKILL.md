---
name: task-conductor
description: Coordinate or adopt tracked delivery across bounded Codex workers, using coordinator-owned subagents for execution and independent tasks for lifecycle boundaries when authorized. Provides explicit dependencies, isolated branches and worktrees, durable handoffs, controlled concurrency, execution-profile accounting, context rollover, and evidence-based acceptance. Use when the user explicitly asks for a coordinator, cross-task orchestration, multiple Codex workers, a controlled parallel pilot, or repository adoption of this workflow. Do not use for ordinary single-task implementation or as implicit authorization to create tasks, trackers, pull requests, deployments, or subagents.
---

# Task Conductor

Coordinate a tracked initiative without making one long task the only source of truth. Keep the coordinator focused on dependencies and acceptance. Give each worker one bounded outcome. Prefer coordinator-owned subagents for automated work inside one delivery lifecycle; use independent user-owned tasks only when their separate lifecycle is material.

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
Read [`references/delegate-to-agy.md`](references/delegate-to-agy.md) only when the user explicitly selects AGY as an implementation executor.

## Repository adoption

- Treat global `AGENTS.md` guidance as optional personal configuration, not an installation requirement.
- Prefer repository-local instructions for shared tracker, verification, Git lifecycle, language, and owner-only rules.
- When the user asks to establish governance and none exists, copy and tailor `assets/task-governance-template.md` into the repository's declared documentation location.
- Do not treat the bundled template as active policy until the repository adopts it.
- Do not copy organization-specific rules from another repository without review.

## 1. Confirm preconditions

- Confirm the initiative has a repository-declared durable tracker or another explicitly authorized durable handoff location.
- If neither exists, report the governance gap. Do not invent a tracker or silently make chat the durable record.
- Confirm the user explicitly authorizes the requested worker topology and concurrency. This skill does not supply authorization to spawn subagents or create independent tasks.
- Select and record one topology before dispatch:
  - `coordinator-owned subagent` is preferred for bounded automated execution and review within the current delivery lifecycle
  - `independent user-owned task` is reserved for direct user follow-up, a separate authorization or risk boundary, long-lived ownership, a distinct host or repository, or explicit user preference
- Record the implementation executor separately from worker ownership: `Codex direct` by default, or `AGY via $delegate-to-agy` only when the user explicitly requests AGY delegation. Authorization for a Codex worker does not authorize sending code to AGY.
- Confirm the selected topology's creation, naming, monitoring, and isolation capabilities before promising orchestration.
- Resolve a saved-project destination only for an independent task. Bind all workers to the canonical repository path and expected host; if more than one independent-task destination remains plausible, stop for explicit selection.
- Keep capability, destination-resolution, inventory, ownership, and creation failures separate. One failure is not evidence that another check passed or failed.
- Treat independent tasks and background subagents as different topologies. Authorization for one does not authorize the other.
- If creation of the authorized topology fails, stop and report the exact failure. Do not silently switch topology, recreate the outcome, or implement worker scope in the coordinator.
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
- implementation executor and external conversation routing when applicable
- integration order
- authorization boundaries
- authorization anchors: the trusted user turn or standing-policy boundary that
  authorizes topology, external disclosure, and each external side effect
- one next action

Maintain one outcome manifest keyed by durable outcome ID. Derive worker, commit,
PR, accepted, and deployed counts from that manifest instead of hand-counting a
range or narrative summary. Reconcile every published identifier back to exactly
one manifest row before closing the initiative.

Keep product specification, lifecycle dashboard, and detailed evidence separate
when the tracker supports it. Do not turn one specification file into an
ever-growing execution transcript. Link stable scope to a compact current-state
record and store verbose logs or artifacts at stable evidence locations.

When work crosses a material risk or product boundary, close or pause the current
outcome and create a newly scoped outcome. Publication, infrastructure changes,
credential work, password-policy changes, deployment, and cleanup are not implicit
continuations of a feature outcome merely because they use the same repository.

Use `references/status-contract.md`. Treat agent paths, task IDs, and the live dashboard as routing data, not durable lifecycle state.

## 3. Name workers and resolve execution profiles

- Title every coordinator, worker, reviewer, and follow-up task or agent as `[project/module] | [bounded outcome] | [role]`.
- Use exactly one independently verifiable outcome in the middle segment. Keep status, dates, sequence-only labels, and task IDs out of titles.
- Pass the title through the worker-creation operation. Rename immediately when creation-time titles are unavailable.
- Record `default/inherited`, or the explicitly selected model, reasoning effort, and rationale.
- Omit model and reasoning overrides by default. Set a model only when the user explicitly requests that model.
- Pass requested overrides through task-creation fields, not prompt prose alone, and verify destination support before dispatch.
- Treat higher effort and additional workers as separate token and latency decisions.
- Treat worker topology and implementation executor as separate decisions. A coordinator-owned Codex subagent may manage an AGY implementation without making AGY a Codex task or subagent.

## 4. Isolate mutating work

- Give every mutating worker a dedicated branch and physical worktree from a pinned base.
- Never assign two mutating tasks to the same branch or worktree.
- Keep the coordinator out of worker implementation scope.
- Declare ownership and permitted lifecycle actions for task environments, caches,
  ports, databases, generated outputs, and other mutable runtime resources. Probe
  an existing environment before use; do not delete, recreate, or normalize it
  unless the packet or a later explicit authorization permits that exact action.
- If dedicated worktrees are unavailable, run mutating outcomes serially in an exclusive checkout or report the limitation. Do not claim safe parallel mutation.
- Follow `references/git-isolation.md` for dispatch, acceptance, integration, and cleanup.
- For an AGY executor, require the clean linked-worktree and single-writer constraints in `references/delegate-to-agy.md`. Keep the AGY wrapper and policy owned by the installed `$delegate-to-agy` skill; do not copy or modify them in the target repository.

## 5. Apply the parallel readiness gate

- Keep one mutating worker as the default.
- Limit the first parallel pilot to two mutating workers.
- Require explicit current authorization for the exact concurrency and every check in `references/parallel-readiness.md` to pass.
- Stop parallel dispatch when dependency, contract, file/object, resource, or authorization overlap appears.
- Accept workers individually, then run the declared integration acceptance gate.

## 6. Dispatch bounded workers

- Prefer a fresh coordinator-owned subagent with a compact packet over loading the coordinator's full history into a worker. Do not use full-history forks when a compact packet is sufficient.
- Apply the context budget gate and send the compact dispatch packet in `references/context-loading.md`. Do not copy full prior-task histories.
- Record the inherited-context choice for every worker. When trusted user
  authorization must be inherited, select the smallest recent-turn slice that
  contains that authorization and supply scope and evidence through the compact
  packet. Before dispatch, verify that the selected slice actually contains the
  authorization-bearing user turn; a fixed turn count is not evidence by itself.
  Treat a full-history fork as an evidenced exception, not the default.
- Declare a model/tool cycle budget and stop condition for every worker and reviewer. A budget limits loops; it does not override required verification.
- When explicitly authorized, declare a correction envelope with exact mutable
  files or components, permitted evidence-driven correction loops, and the single
  broad-gate allowance. Corrections inside that envelope do not need artificial
  per-line follow-up outcomes. Scope, risk-boundary, credential, deployment, and
  destructive changes still require new authorization.
- On every dispatch, record requested topology, creation operation, returned agent path or task ID, parent lineage when available, and observed topology. Do not infer topology from sidebar placement or a generic `thread_source` label alone.
- For a subagent, retain its agent ID or path as transient routing data and use the parent workflow's bounded wait, message, follow-up, and interruption controls.
- For an independent task, treat a client-side or pending creation handle as evidence that the request was accepted, not that setup is still running or complete. Do not submit the request again. Record `creation accepted / formal ID unresolved / execution unknown` until the formal task ID is correlated.
- For an independent task, resolve the formal task ID with a supported mapping or status capability when available. A missing recent-inventory entry alone does not prove that setup is pending or that execution has not started. Respect inventory bounds and corroborate ownership with Git and durable state.
- Require the worker to inspect current durable state before editing and to return the worker completion contract.
- When the executor is AGY, dispatch a Codex worker with an explicit instruction to use `$delegate-to-agy`. The Codex worker owns baseline capture, AGY invocation, independent diff review, validation, and bounded remediation; the coordinator does not accept AGY's response or terminal status as delivery evidence.
- For AGY, separate an economics-based hard cap from the per-loop convergence
  checkpoint. A user may deliberately authorize a higher cap for a lower-cost
  executor; continue only while new evidence shows progress and keep AGY and Codex
  usage accounting separate.
- Do not allow workers to create nested tasks or subagents unless the user explicitly authorizes that additional topology.
- Use and tailor the templates in `references/task-prompts.md`.

## 7. Monitor with bounded waits

- Prefer cursor-based bounded waits or snapshots. Do not repeatedly reread full task histories.
- For concurrent workers, wait on all active routing IDs in one bounded snapshot when supported.
- Notify the user only for meaningful state changes, decisions, failed acceptance, or completion.
- Keep unaffected workers running when an unrelated worker fails. Stop the batch when shared contract, base, resource, or authorization state drifts.
- Use a follow-up only when outcome and Definition of Done remain unchanged. Track material scope changes as new outcomes.

## 8. Accept evidence, not summaries

Apply the review readiness gate before spending a separate review cycle. Give the reviewer a compact acceptance packet rather than worker history or raw logs.

Require an immutable commit, content-addressed tree, or explicitly recorded stable
diff hash before formal acceptance review. A pre-commit inspection may identify
findings, but it is not the formal acceptance target and must not be followed by a
second broad review merely to discover that the target was mutable.

Freeze the exact repository-wide candidate gate before dispatch. For a single
worker, run every required candidate check on the immutable target before formal
review and delivery acceptance. When a required gate can run only after combining
outcomes, keep the initiative at `integrating` until the shared gate passes. Do not
publish an `accepted` claim or close the outcome first. Treat any later required-gate
failure as an escaped acceptance defect and record its rework separately.

Assign validation ownership before dispatch. Workers normally run objective-
specific semantic probes and focused checks; the actor that creates or owns the
immutable candidate runs the frozen repository-wide gate once. Run the integrated
gate once after combined outcomes. Repeat a broad gate in both worker and
coordinator only when repository policy, a relevant intervening change, or the
declared risk requires it, and record that reason.

Independently verify:

- expected repository, branch, worktree, and final HEAD
- pinned-base ancestry, scoped diff, and clean worktree
- required tests and repository verification gates
- durable tracker Definition of Done
- unresolved review, conflict, security, deployment, or owner-only boundaries

Mark an outcome accepted only when evidence is sufficient. Worker confidence is not evidence.

For a release that combines several outcomes and crosses into migration or live
deployment, prefer one final read-only integrated reviewer after the immutable
integration gate when risk warrants independent assurance. Do not create one
reviewer per outcome by default or repeat the same broad gate solely to add an
actor.

## 9. Stop and hand off

Stop when the initiative is complete, a dependency requires user authority, or remaining work cannot be safely split. Write accepted and blocked outcomes, evidence, execution profiles, decisions, topology, and one next action to the durable tracker. Do not create a competing coordinator backlog.

When the coordinator approaches compaction, becomes difficult to audit, or Codex surfaces a continuation or replacement task, apply the context-rollover protocol in `references/context-loading.md`. Do not depend on an undocumented numeric context threshold. A sidebar thread may be a surfaced subagent rather than an independent task; verify creation and lineage before assigning ownership. The successor coordinator must adopt durable state and active worker IDs without redispatching existing work.

Before publication, enumerate the exact authorized side effects: push, pull-request
creation, merge, reconciliation, deployment, and cleanup. A standing policy may
satisfy authorization only within its exact boundary; it does not permit widening
a narrower current-turn statement. If the announced action list changes after a
policy read, stop and restate or obtain authorization before acting.

After delivery acceptance, apply the delivery-to-Ops boundary in `references/context-loading.md`. Continue only for an already authorized bounded handoff; otherwise propose a separately authorized Ops outcome. Use an independent Ops task when its lifecycle must be user-owned; otherwise an explicitly authorized subagent may perform bounded Ops work under the current coordinator. Give either topology its own packet and measurement cutoff.

Freeze and record the delivery manifest, accepted target, elapsed-time cutoff,
and token counters before the first publication, migration, deployment, or live
operation. A same-turn continuation does not remove this boundary. Prefer a
coordinator rollover at this point when compaction has occurred or the remaining
Ops work is material.

Record token and elapsed-time telemetry when available, but do not invent missing values or claim causation from one observation.
