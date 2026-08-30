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

- [x] Complete one clean-room serial pilot with a coordinator-owned Codex
  subagent and independent coordinator acceptance.
- [x] Complete one serial independent-task pilot from a fresh coordinator context.
- [x] Verify the worker is a user-owned independent task, not a background subagent.
- [x] Exercise a task-creation failure and confirm the coordinator stops instead of changing topology.
- [x] For a multi-dispatch pilot, confirm the creation operation and returned independent task ID separately for every worker.
- [x] Exercise an out-of-range inventory request and confirm it is reported as `unknown` ownership, then safely retried within the active runtime bound.
- [x] Confirm ownership uses recent inventory, known task IDs, Git state, and the durable tracker rather than one bounded list alone.
- [x] Exercise an ambiguous saved-project mapping and confirm destination failure remains separate from inventory and ownership results.
- [x] Resolve an ambiguous destination by explicit selection, refresh it before dispatch, and confirm cleanup is not incorrectly required when every ownership source is `clear`.
- [x] Exercise asynchronous task creation and confirm a client-side handle does not trigger a duplicate creation request or subagent fallback.
- [ ] Exercise a case where the formal task exists but recent-task inventory omits it; confirm the coordinator reports `formal ID unresolved / execution unknown`, not `setup pending` or `worker not started`.
- [x] Supply a formal task ID through an independent trusted surface and confirm destination, title, repository, branch, and worktree metadata are verified before monitoring.
- [x] Capture a fixed start, cutoff, included roots/descendants, outcome states, model/effort, token categories, and elapsed-time definition.
- [x] Complete a serial pilot where the full frozen repository-wide candidate gate
  passes on the immutable target before acceptance and publication.
- [x] Exercise environment ownership preflight and confirm unapproved deletion,
  recreation, normalization, and cleanup stop before mutation.
- [x] Exercise publication authorization with push, PR, merge, reconciliation, and
  cleanup enumerated separately; confirm a narrower current-turn statement is not widened.
- [x] For a stable parallel claim, complete a controlled two-worker pilot with every parallel readiness gate satisfied and an integration acceptance gate.

Operational evidence (2026-08-13): Pilot 1 used a retained root coordinator with
no parent context and four serial independent worker roots. Its later recovery
exercise covered the bounded inventory retry, separate destination and inventory
failures, multi-source ownership, explicit destination selection, one asynchronous
creation request, and externally supplied formal-ID verification. Pilot 2
completed one serial user-owned worker and reviewer flow through independent
acceptance. The historical runs did not pass the three failure-path checks later
closed by the separate controlled exercise below; rules added after retrospective
analysis were not treated as execution evidence by themselves.

Failure-path evidence (2026-08-13): a controlled invalid-destination request was
rejected without creating a task; the coordinator stopped that dispatch path and
did not substitute another topology. Two later read-only independent reviewers
were dispatched serially from the same pinned commit into separate clean detached
worktrees. Each successful creation first returned a client-side handle, remained
absent from an immediate bounded inventory snapshot, and surfaced under a formal
task ID after a later snapshot. This proves correct unknown-state and no-duplicate
handling, but it does not prove that the formal task records already existed during
the first omissions. A separate fresh attempt authorized after the measurement
cutoff found its formal task in the first bounded inventory snapshot, so the exact
formal-task-exists/inventory-omits race remains unverified. The coordinator
submitted each creation request once and verified each resolved formal task and
worktree independently. A malformed project ID on the second reviewer was retried
exactly once only after refreshing the unique destination and confirming that the
failed request created nothing. The first reviewer required one same-outcome
follow-up because the coordinator supplied an incomplete canonical path; the
worker stopped rather than expanding scope.

The measurement window ran from explicit authorization at
`2026-08-13T06:14:52+08:00` through independent evidence verification at
`2026-08-13T06:21:28+08:00` (6m 36s wall-clock). Aggregate reported usage was
4,899,004 tokens: 4,884,244 input, including 4,776,448 cached input, plus 14,760
output; reasoning output was a 4,109-token subset. The coordinator used 4,595,093
incremental tokens, while the two reviewer roots used 232,271 and 71,640. This
failure-path observation reused a long-running coordinator, so its 93.8% share is
not a fresh-context baseline or evidence about normal delivery efficiency. Active
model time and tool-wait time were unavailable. The separately authorized
post-cutoff attempt and its child reviewer are excluded from these totals.

Subagent and parallel evidence (2026-08-20): an isolated local fixture pinned one
base and assigned non-overlapping files to coordinator-owned workers. The serial
direct outcome produced one immutable commit and passed independent path, content,
ancestry, whitespace, and cleanliness checks. Both concurrent workers then
produced one isolated commit each. The coordinator independently accepted both,
integrated them in the declared A-then-B order, and passed the frozen two-file
integration gate on a clean worktree. This validates controlled concurrency and
integration acceptance, not token savings or hardware-level simultaneous
execution. Worker token and active-time telemetry were unavailable.

Forward lifecycle evidence (2026-08-31): one authorized vertical-slice delivery
used a serial foundation pilot, two non-overlapping feature workers, one
integration writer, two independent reviewers, and one bounded correction
worker. The immutable product target passed the complete repository quick and
delivery gates before publication. Runtime preflight reused declared Python and
Node environments without rebuilding or normalizing them, and cleanup stopped
safely when live Windows handles retained empty directories and a preserved ref.
Publication authorization enumerated issue, branch, worktree, commit, push, PR,
merge, reconciliation, and cleanup actions. Three CI-verified PRs merged, although
the second tracker-only finalization exposed a recursive reconciliation pattern
that the unreleased guidance now prohibits by default. See
`field-observation-subagent-delivery-lifecycle.md`.

## Publication

- [x] Choose the release level honestly: remain `preview` while the recorded
  inventory-correlation and forward-guardrail gaps remain open.
- [x] Replace installation placeholders with the canonical public GitHub URL.
- [x] Create a signed or annotated version tag and GitHub release notes from `CHANGELOG.md`.
- [x] Reinstall from the published tag and repeat the recognition smoke test.
- [x] Run one clean-room Task Conductor pilot with a coordinator-owned Codex worker
  using the separately installed `$delegate-to-agy` executor contract.

Release evidence (2026-08-20): annotated tag `v0.1.0-preview` resolves to commit
`a09de3b0ecc76ac5a7fa5e32555377de32d72658`. GitHub published it as a non-draft
prerelease using `docs/release-v0.1.0-preview.md`. The official installer then
downloaded `skills/task-conductor` from that tag. All 11 installed files matched
the tagged source by SHA-256, and the official validator returned
`Skill is valid!`.

A fresh ephemeral `codex-cli 0.148.0` process ran in read-only mode, explicitly
loaded `$task-conductor`, correctly summarized the subagent-first topology,
independent-task boundary, AGY authorization boundary, and context-rollover rule,
and made no tool call or dispatch. It reported 22,082 input tokens and 245 output
tokens, including 65 reasoning-output tokens, over a 20.1-second observed command
window. This is release-recognition telemetry, not delivery-performance evidence.

AGY pilot evidence (2026-08-20): the authorized coordinator-owned Codex worker
passed AGY executable, version, repository, branch, base, ancestry, and clean
worktree preflight. The separately installed `$delegate-to-agy` wrapper then
failed its own Git change inspection before AGY launched; validation-only mode
failed at the same boundary while the equivalent standalone Git commands passed.
No AGY conversation, tracked change, remediation pass, or commit was created, so
at that cutoff the publication item remained unchecked and the outcome was
`needs_followup`.

AGY follow-up evidence (2026-08-21): the wrapper failure was traced to a linked
worktree created under the sandbox identity and inspected under the host identity,
not to flattened PowerShell argument arrays. The separately maintained wrapper
added command-scoped `safe.directory` only for its derived workspace, passed its
original validation-only reproduction, was published, reinstalled from the
immutable commit, and matched all 11 published Git blobs. AGY 1.1.16 then launched
in a fresh conversation but returned `ERROR` after its sandbox denied an attempted
PowerShell byte-check command. It left only the allowed marker file changed, but
with CRLF instead of the required LF. Because a failed run left a tracked partial
change, the worker correctly performed no retry, remediation, normalization, or
commit. The private conversation ID is intentionally omitted.

Second AGY follow-up evidence (2026-08-21): after explicit recovery authority,
the coordinator restored the sole partial file to the pinned base and clarified
that AGY should use only its workspace edit tool while Codex owned byte
verification. Installed-wrapper validation passed with a fresh task and no cache
hit. AGY 1.1.17 returned `SUCCESS` and changed only the allowed file, but Codex
again found CRLF instead of the required LF. The worker created a valid
same-conversation remediation packet; the wrapper rejected it before contacting
AGY because the successful implementation receipt binds the implementation task
hash while remediation necessarily has a new task hash. No remediation pass or
commit occurred, and the private conversation ID remains omitted.

Third AGY follow-up evidence (2026-08-21): a separately authorized wrapper repair
admitted receipt-bound remediation only when receipt status, prior task SHA format,
conversation identity, current output hashes, and current write scope all agreed.
The repair passed the real blocked packet, official validation, publication,
reinstallation, and all 11 published-blob comparisons. The same-conversation AGY
1.1.17 remediation then changed the file to the correct LF bytes, but terminal
JSON status was `ERROR` because AGY's later fuzzy fallback reported no net diff
and could not find the old target content. Independent Codex checks confirmed the
correct 9-byte file, sole changed path, and clean diff, but the receipt still
binds the prior implementation task. The frozen contract therefore prohibited a
commit or acceptance.

Fourth AGY follow-up evidence (2026-08-21): the coordinator preserved the failed
remediation evidence, restored the sole tracked file to the pinned base, and
created a fresh `implement` task with no conversation reuse. Installed-wrapper
validation passed with one write path, no cache hit, and no remediation baseline.
AGY 1.1.17 returned terminal `SUCCESS` in one turn, and the new receipt correctly
bound the current task and actual output. Independent Codex checks nevertheless
measured `6167792D706173730D0A` (10-byte CRLF), not the frozen
`6167792D706173730A` (9-byte LF) contract. Scope, ancestry, and whitespace checks
passed, but no commit or automatic retry was permitted. The private conversation
ID remains omitted.

Portable-EOL AGY pilot evidence (2026-08-21): a newly scoped fixture base added
`src/*.txt text eol=lf` and changed the portable byte gate from mutable Windows
worktree bytes to the immutable committed blob. The initial file materialized as
LF in a fresh linked worktree. Two wrapper launches were stopped before process
creation because the original worker did not directly inherit the later trusted
user authorization; coordinator-relayed authorization was correctly rejected.
An explicitly authorized replacement worker then reached AGY but received
eligibility-check `503 UNAVAILABLE` with zero turns, zero tokens, no conversation,
no receipt, and no changes. The one separately authorized fresh retry used a new
replacement worker that directly inherited the user authorization. AGY 1.1.17
returned terminal `SUCCESS` in one turn, and the worker created immutable commit
`57202c365a2fc22721989605da9a8de6d3337a3f`. Coordinator acceptance verified the
current receipt's task and output bindings, pinned-base ancestry, exactly
`src/agy.txt` committed, no `.agy` artifact, clean whitespace and tracked state,
blob `8fa3b154de706ac4bf672151e0d9c97a74358cdb`, size 9, and exact bytes
`6167792D706173730A`. The successful retry reported 41,359 input, 1,895 output,
1,465 thinking, 24,409 cache-read, and 43,254 total tokens over 11.010 seconds;
Codex token and active-time telemetry were unavailable. Private conversation IDs
remain omitted. No push, merge, PR, deployment, or cleanup occurred.

## Remaining preview blockers

- A fresh case where a formal task already exists while bounded inventory omits it has not yet been reproduced.
- The newly added single broad-gate owner, adaptive monitoring, finite
  reconciliation, and lifecycle-facet controls have not yet passed a clean
  forward pilot.
