# Release checklist

Use this checklist for a preview or stable Task Conductor release. Record failures as release blockers; do not turn an unverified capability into a claim.

## Repository hygiene

- [x] `README.md`, `CHANGELOG.md`, `LICENSE`, adoption guidance, and the case study agree on the release status.
- [x] Skill frontmatter has only `name` and `description`, and the name is `task-conductor`.
- [x] No session IDs, raw conversation logs, credentials, private repository names, customer data, or production details are tracked.
- [x] Examples use placeholders and do not imply authorization to create tasks or mutate external systems.
- [x] `git diff --check` passes and the intended release files are the only changed files.

Hygiene evidence (2026-08-13): all 17 intended public files were scanned because
the repository still had an unborn `HEAD`; `.codex-cache/` remained ignored.

## Skill validation

- [x] Run the current official skill validator against `skills/task-conductor`.
- [x] Resolve every schema or YAML error; do not skip validation because a local dependency is missing.
- [x] Confirm every relative link and required reference resolves from `SKILL.md`.
- [x] Confirm `agents/openai.yaml` still describes the same trigger boundary as `SKILL.md`.

Validation evidence (2026-08-13): the bundled official `quick_validate.py`
returned `Skill is valid!` in an isolated environment with PyYAML.

## Clean-room installation

- [x] Install from the exact Git commit or tag intended for release into a clean Codex environment.
- [x] Restart or reload the client and confirm `$task-conductor` is discoverable.
- [x] Ask it to summarize authorization, durable tracker, isolation, topology, and acceptance rules without dispatching work.
- [x] Confirm uninstalling or disabling the skill leaves no repository policy behind.

Clean-room evidence (2026-08-13): the installer downloaded commit
`63c306b9d66711e4487e1f7eb1a8233932387aaa` into an isolated repository skill
scope. The installed tree matched all 10 committed blobs and passed the official
validator. A fresh ephemeral Codex CLI 0.147.0 process using `gpt-5.6-sol` with
reasoning effort `none` explicitly invoked the skill, loaded its `SKILL.md`,
summarized every requested boundary, and performed no tool call or dispatch. The
process reported 7,062 tokens and 13.614 seconds wall-clock; this is recognition
smoke-test telemetry, not delivery-performance evidence. Removing the
repository-scoped skill link left no instruction or governance file behind.

## Operational pilots

- [x] Complete one serial independent-task pilot from a fresh coordinator context.
- [x] Verify the worker is a user-owned independent task, not a background subagent.
- [ ] Exercise a task-creation failure and confirm the coordinator stops instead of changing topology.
- [ ] For a multi-dispatch pilot, confirm the creation operation and returned independent task ID separately for every worker.
- [x] Exercise an out-of-range inventory request and confirm it is reported as `unknown` ownership, then safely retried within the active runtime bound.
- [x] Confirm ownership uses recent inventory, known task IDs, Git state, and the durable tracker rather than one bounded list alone.
- [x] Exercise an ambiguous saved-project mapping and confirm destination failure remains separate from inventory and ownership results.
- [x] Resolve an ambiguous destination by explicit selection, refresh it before dispatch, and confirm cleanup is not incorrectly required when every ownership source is `clear`.
- [x] Exercise asynchronous task creation and confirm a client-side handle does not trigger a duplicate creation request or subagent fallback.
- [ ] Exercise a case where the formal task exists but recent-task inventory omits it; confirm the coordinator reports `formal ID unresolved / execution unknown`, not `setup pending` or `worker not started`.
- [x] Supply a formal task ID through an independent trusted surface and confirm destination, title, repository, branch, and worktree metadata are verified before monitoring.
- [x] Capture a fixed start, cutoff, included roots/descendants, outcome states, model/effort, token categories, and elapsed-time definition.
- [ ] For a stable parallel claim, complete a controlled two-worker pilot with every parallel readiness gate satisfied and an integration acceptance gate.

Operational evidence (2026-08-13): Pilot 1 used a retained root coordinator with
no parent context and four serial independent worker roots. Its later recovery
exercise covered the bounded inventory retry, separate destination and inventory
failures, multi-source ownership, explicit destination selection, one asynchronous
creation request, and externally supplied formal-ID verification. Pilot 2
completed one serial user-owned worker and reviewer flow through independent
acceptance. The historical runs did not pass the three unchecked failure-path
checks above; rules added after retrospective analysis are not execution evidence.

## Publication

- [x] Choose the release level honestly: `preview` while clean-room or parallel validation remains pending; stable only after the claimed capabilities pass.
- [x] Replace installation placeholders with the canonical public GitHub URL.
- [ ] Create a signed or annotated version tag and GitHub release notes from `CHANGELOG.md`.
- [ ] Reinstall from the published tag and repeat the recognition smoke test.

## Current v0.1.0-preview blockers

- Stop-on-creation-failure behavior has not yet been revalidated after the topology fallback defect.
- Per-dispatch creation-operation and independent-task-ID verification has not yet passed a fresh multi-dispatch pilot.
- The corrected `formal ID unresolved / execution unknown` report has not yet been reproduced in a fresh correlation-race exercise.
- Controlled two-worker parallel execution has not yet been validated.
