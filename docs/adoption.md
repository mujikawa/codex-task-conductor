# Adopting Task Conductor

Task Conductor supplies a reusable orchestration workflow. It does not replace personal preferences, repository rules, or the team's durable tracker.

## Instruction layers

| Layer | Put here | Keep out |
| --- | --- | --- |
| Global `AGENTS.md` | Optional personal defaults used across repositories, such as language and requiring explicit authorization for task creation | Repository commands, branch names, tracker locations, or team-specific owner rules |
| Repository `AGENTS.md` | Shared verification gates, tracker policy, branch and worktree lifecycle, repository boundaries, and owner-only actions | Personal preferences and duplicated Task Conductor procedures |
| Task governance document | Durable tracking triggers, lifecycle states, handoff requirements, ownership, and closure rules | Implementation details already owned by the repository guide |
| Task Conductor skill | Bounded dispatch, monitoring, isolation, parallel readiness, and evidence-based acceptance | Organization-specific policy that the repository has not adopted |

Codex loads optional global guidance from `$CODEX_HOME/AGENTS.md` and then layers project guidance from the repository root toward the working directory. More specific project guidance appears later and can override broader guidance. See the official [AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md).

Installing Task Conductor must not require changing global guidance. Prefer repository-local adoption for rules the whole team should share.

## Optional global guidance

Keep global guidance short. For example:

```md
## Cross-task coordination

- When I explicitly request cross-task orchestration, use `$task-conductor`.
- Do not spawn subagents, create independent tasks, or increase concurrency without explicit authorization.
- Propagate my requested output language to every dispatched task.
```

Do not add this snippet when those preferences are not truly global.

## Repository guidance

Add or adapt a concise section in the repository's canonical instruction file:

```md
## Task continuity

- Canonical tracker: [system and location].
- Track work that crosses sessions or has an independent Definition of Done.
- Keep stable scope in the tracker and progress in its activity history.
- A tracker does not authorize deployment, destructive operations, or credential changes.

## Verification

- Required worker gate: [commands].
- Required integration gate: [commands].

## Git isolation

- Assign one mutating task to each branch and physical worktree.
- Worktree location and lifecycle: [policy].
- Owner-only Git operations: [operations].
```

Keep exact commands and authorization boundaries in the repository, where every contributor can review them. Do not copy another organization's rules without adapting them.

## Task governance

Copy `skills/task-conductor/assets/task-governance-template.md` into the repository's documented governance location and replace every bracketed field. The template is inert until the repository adopts it through its normal review process.

Choose one canonical tracker. GitHub Issues, Linear, Jira, and another team-owned system are all valid when they preserve stable scope, activity history, ownership, acceptance evidence, and one next action. A local file is a fallback only when the repository explicitly permits it.

## Capability check

Record the actual capabilities of the Codex surface before the first pilot:

| Capability | Preferred behavior | Safe fallback |
| --- | --- | --- |
| Spawn and manage subagents | Use one bounded coordinator-owned worker, retain its agent path, and monitor with bounded waits | Run the outcome directly only when it no longer needs a coordinator; otherwise stop |
| Create and title independent tasks | Use only for a material user-owned lifecycle boundary; verify the returned independent task ID | Produce a prompt for the user to create manually; do not silently change topology |
| Delegate implementation to AGY | Require an explicit `$delegate-to-agy` request, a clean linked worktree, one writer, and the installed skill's validated wrapper | Use Codex direct execution or stop; do not recreate the wrapper or silently send code externally |
| Select model and reasoning effort | Omit overrides by default; pass explicit user choices through task creation | Record `default/inherited` |
| Monitor task state | Use bounded cursor-based waits or snapshots | Ask workers to update the durable tracker and check at explicit milestones |
| Inventory current ownership | Use the active runtime's accepted query bound, known task IDs, Git state, and the durable tracker | Classify ownership as `unknown` and stop dispatch |
| Create worktrees | Give every mutating worker a dedicated worktree | Run mutating outcomes serially in one exclusive checkout |
| Use a durable tracker | Read and update the repository-declared system | Stop or use only an explicitly authorized local fallback |

Missing capabilities must reduce the claimed workflow. Do not describe manual dispatch as automated orchestration or concurrent dispatch as actual parallel execution.

Independent tasks and background subagents are not interchangeable. Prefer a
subagent for bounded automation within one delivery lifecycle: the coordinator can
spawn, monitor, follow up, and collect its result directly. Use an independent task
when direct user follow-up, separate authorization or risk, long-lived ownership,
a distinct host or repository, or explicit user preference makes its independent
lifecycle material. If the authorized creation call fails, changing topology
requires new explicit authorization because visibility, cancellation, context,
and lifecycle semantics change.

Worker ownership and implementation executor are also separate. A
coordinator-owned Codex subagent can manage AGY through `$delegate-to-agy`; AGY
does not become a Codex task or durable owner. Keep the delegation skill installed
and maintained separately rather than copying its executable wrapper or policy
into this repository. Record the AGY conversation ID in private routing state when
the canonical tracker is public. See the
[AGY integration contract](../skills/task-conductor/references/delegate-to-agy.md).

Codex may surface subagent threads in the sidebar or continue work after context
compaction. UI placement alone does not turn a parent-owned subagent into an
independent task. Before a coordinator rollover, checkpoint the durable tracker,
active routing IDs, Git and resource ownership, decisions, and one next action. A
successor coordinator adopts that checkpoint and reconciles live workers once; it
does not redispatch them.

Do not classify topology from a field such as `thread_source` by itself. Prefer the creation operation and returned task ID. For forensic telemetry, corroborate that evidence with parent lineage and agent-path metadata when available.

Task inventory is a bounded discovery aid, not a complete ownership registry. Respect the active runtime's validation limits and do not hard-code an observed maximum as a permanent product contract. If inventory is rejected or incomplete, ownership remains `unknown`. Combine recent inventory with direct checks of known task IDs, Git worktree and branch state, the durable tracker, and shared-resource ownership. See the [dispatch troubleshooting guide](../skills/task-conductor/references/troubleshooting.md).

Duplicate saved-project metadata does not always require immediate cleanup. Explicitly bind the intended destination, refresh and verify it before every dispatch, exclude the duplicate, and require every ownership source to report `clear`. When asynchronous task creation returns a client-side handle, preserve it and do not create a duplicate worker. Until the formal task ID is correlated, report `creation accepted / formal ID unresolved / execution unknown`; absence from recent-task inventory is not a setup-status signal.

## Team rollout

1. Agree on the canonical tracker and authorization boundaries.
2. Adopt repository-local instructions and the tailored governance document through normal review.
3. Install the skill for pilot participants.
4. Run one serial coordinator-owned subagent through dispatch, handoff, and independent acceptance.
5. Record the operational baseline and correct any governance gaps.
6. Authorize at most two mutating workers for the first parallel pilot only after every readiness check passes.
7. Keep, revise, or remove the workflow based on comparable delivery evidence.

## Verification

Start a fresh Codex run in the target repository and ask it to summarize the active instructions, tracker, verification gate, Git isolation rule, and owner-only actions. Correct missing or conflicting guidance before dispatching a worker.

Do not use successful instruction loading as proof that repository permissions, external tools, or task-management capabilities are available. Verify those separately.
