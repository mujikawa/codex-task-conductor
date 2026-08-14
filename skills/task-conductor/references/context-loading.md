# Context-loading contract

Bound context by controlling what each task receives, rereads, and returns. These
rules govern workflow inputs and cycles; they do not claim that Codex Desktop can
directly control prompt caching, `reasoning.context`, or compaction thresholds.

## Contents

- Context budget gate
- Compact dispatch packet
- Model/tool cycle budget
- Review readiness gate
- Compact acceptance packet
- Input reduction rules
- Delivery-to-Ops boundary

## Context budget gate

Before dispatch, review, or acceptance:

1. Name the decision the next task must make.
2. Include only material needed for that decision: current contract, exact target,
   unresolved risks, and evidence locations.
3. Replace prior conversation, repeated status, and raw logs with a compact packet.
4. Link to authoritative files or tracker sections instead of copying them. Include
   excerpts only when the exact text is necessary.
5. Classify the packet:
   - `ready`: every item supports the next decision and no required input is missing
   - `trim`: duplicated, historical, or discoverable content is embedded
   - `blocked`: the packet cannot identify authoritative state or required evidence

Dispatch or accept only at `ready`. Trim before proceeding; resolve `blocked` from
durable sources rather than adding speculative context.

## Compact dispatch packet

Send one packet per bounded outcome:

- outcome and one-sentence purpose
- durable tracker location and current state anchor
- satisfied dependencies and pinned base
- in scope, out of scope, and Definition of Done
- dedicated branch, worktree, and mutable-resource ownership
- environment, cache, port, database, and generated-output ownership plus allowed
  create, reuse, rebuild, normalize, and cleanup actions
- required validation and evidence locations
- authorization boundaries and declared execution profile
- model/tool cycle budget and stop conditions
- one next action

Do not attach full coordinator history, entire Issue discussions, unrelated diffs,
raw test logs, or artifacts that the worker can locate from an exact reference.

## Model/tool cycle budget

- Declare a task-specific budget before dispatch for inspection, implementation,
  focused verification, and at most the authorized correction loops.
- Use reported model/tool cycles when available. Otherwise use observable action
  loops—inspect, change, verify, reassess—as an explicitly labeled proxy.
- Start with the smallest budget credible for the outcome. Increase it only from
  new evidence, not because a task is repeatedly rereading unchanged state.
- At the budget boundary, stop the loop and return current evidence, remaining gap,
  and one next action. Do not silently raise effort, add workers, or rerun broad
  checks.
- Reset the budget only for a newly scoped outcome or explicitly authorized
  follow-up. Preserve the original Definition of Done for a same-scope follow-up.
- Count product correction loops, infrastructure recovery attempts, review cycles,
  publication cycles, and full-gate reruns separately. A recovery may be exempt
  from the product-change budget, but never from telemetry or stop conditions.

### Correction envelope

Prefer one explicit correction envelope over repeated micro-authorization when the
user and repository policy permit it. Record:

- exact files, components, and behavior that may change
- the maximum evidence-driven correction loops
- focused checks after each correction
- the one allowed broad-gate run after focused checks pass
- conditions that immediately end the envelope

The envelope ends on material scope drift, a new external side effect, credential
or permission work, deployment risk, destructive cleanup, or exhausted loops. It
does not convert a bounded outcome into open-ended authority.

## Review readiness gate

Create or start an independent review only when all checks pass:

- the worker identifies the immutable review target and dedicated isolation state
- the review target is a commit, content-addressed tree, or recorded stable diff
  hash accepted by repository policy; an ordinary mutable working tree is not a
  formal acceptance target
- the scoped diff is stable and contains no unexplained files
- required focused checks have exact results and evidence locations
- the frozen repository-wide candidate gate has passed on the immutable target, or
  the outcome remains `integrating` because a declared shared gate requires combined state
- the durable tracker and Definition of Done agree with the claimed outcome
- unresolved failures, skipped checks, generated artifacts, and owner-only actions
  are explicit
- the compact acceptance packet can be assembled without reconstructing worker chat

If any check fails, keep the outcome at `needs_followup`; request only the missing
evidence or correction. Do not spend a reviewer cycle rediscovering incomplete work.

## Compact acceptance packet

Give the reviewer or coordinator:

- outcome, Definition of Done, and immutable review target
- changed-file manifest and concise rationale
- scoped diff summary plus exact locations for decision-critical hunks
- required test/check results, including failures and skips
- artifact manifest with only decision-relevant views or sections
- unresolved risks, authorization boundaries, and durable tracker state
- execution-profile and telemetry availability
- requested decision: `accept` or `needs_followup`

The acceptance packet routes verification; it does not replace independent checks.
Record the final decision and evidence in durable state, not by preserving chat.

## Input reduction rules

- **Tests:** Run the narrowest relevant checks first. Retain command, exact result,
  and a short failure excerpt. Load full logs only to diagnose a current failure.
  Run each required broad gate once after focused checks pass, and rerun it only
  after a relevant change or an inconclusive infrastructure failure.
- **Diffs:** Start with base/HEAD, status, changed-file names, and diff statistics.
  Load targeted hunks for contract, risk, or failure analysis. Load the full diff
  only when scope is small or the acceptance decision requires cross-file review.
- **Issues and trackers:** Load the current outcome, Definition of Done, decisions,
  blockers, and latest authoritative state. Do not replay the full comment history
  unless a named decision depends on it. Refer to public examples with placeholders;
  never publish private identifiers.
- **Artifacts:** Start from a manifest containing type, location, version or hash,
  and purpose. Inspect only decision-relevant pages, frames, sections, or samples.
  Preserve required visual or generated-output verification, but do not embed an
  entire artifact when a stable location and selected evidence suffice.

Reduction never removes a repository-required check, evidence needed for safety, or
information necessary to reproduce a failed acceptance.

## Delivery-to-Ops boundary

After delivery acceptance, classify the next action before continuing:

- Keep it in the current task only when it is a bounded recording or handoff action
  already authorized and uses the same risk boundary.
- Propose an independent Ops task when work changes authorization, credentials,
  environment, tools, rollback needs, live-system risk, or monitoring duration—for
  example publication, merge, deployment, migration, or production observation.
- Do not create the Ops task without explicit authorization. Give it a new compact
  dispatch packet, execution budget, durable state, and measurement boundary.
- Enumerate push, PR creation, merge, reconciliation, deployment, and cleanup
  separately. Do not widen a narrower action list announced in the current turn by
  later relying on standing policy; restate or request authorization first.
- If no Ops task is authorized, stop after recording the owner action and evidence.


Start a new outcome when an Ops phase adds a new product or infrastructure change,
such as transport topology, account-provisioning mode, password policy, credential
rotation, or repository cleanup. Do not accumulate these changes under the title
and measurement boundary of the original feature delivery.
