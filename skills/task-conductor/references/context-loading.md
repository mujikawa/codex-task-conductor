# Context-loading contract

Bound context by controlling what each task receives, rereads, and returns. These
rules govern workflow inputs and cycles; they do not claim that Codex Desktop can
directly control prompt caching, `reasoning.context`, or compaction thresholds.

## Contents

- Context budget gate
- Compact dispatch packet
- Trust-preserving inheritance
- Model/tool cycle budget
- Layered validation ownership
- Review readiness gate
- Compact acceptance packet
- Input reduction rules
- Context rollover
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
- inherited-context selection, authorization anchor, and the trusted user turn or
  policy boundary it must preserve
- implementation executor; for AGY, include the allowed paths, AGY cycle budget,
  and location of the private conversation-routing record
- model/tool cycle budget and stop conditions
- one next action

Do not attach full coordinator history, entire Issue discussions, unrelated diffs,
raw test logs, or artifacts that the worker can locate from an exact reference.
When the creation surface supports selecting inherited turns, use no inherited
history or the smallest recent slice that contains indispensable trusted user
authorization. Do not use a full-history fork merely for convenience. Put scope,
state, and evidence in the compact packet; preserve direct user authorization only
through a supported trusted-input mechanism.

## Trust-preserving inheritance

Choose inherited context separately from the dispatch packet:

- use no inherited turns when the packet and durable sources are sufficient;
- use the smallest recent-turn slice that directly includes indispensable user
  authorization when the worker or its external executor must prove trusted
  authorization at a host boundary;
- use full history only when a narrower supported slice cannot preserve the
  required trust or decision context.

Record the selection, the authorization-bearing turn or boundary it preserves,
and why a narrower option was insufficient. Verify the selected slice contains
that trusted input before dispatch; recording `3 turns` or another numeric slice
alone is not proof. For external executors, also record the exact private paths or
content classes the authorization permits disclosing. Do not copy the same
history into the packet. Full-history inheritance is a measurable context-cost
decision, not a substitute for a complete scope packet.

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

## Layered validation ownership

Declare one owner for each validation layer before dispatch:

- the worker runs objective-specific semantic probes and the narrowest checks
  needed to find implementation defects;
- the immutable-candidate owner runs the frozen repository-wide candidate gate
  once after focused checks pass;
- the coordinator runs the integration gate once after outcomes are combined.

Do not automatically run the same broad gate in both a mutable worker worktree and
again in coordinator acceptance. A second broad run requires a relevant code or
environment change, an inconclusive infrastructure failure, repository policy, or
an explicit risk rationale. Record sandbox-to-host retries as one logical gate with
separate attempts, not as independent product-validation cycles.

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

- **Tests:** Run objective-specific semantic probes and the narrowest relevant
  checks first. Retain command, exact result,
  and a short failure excerpt. Load full logs only to diagnose a current failure.
  Run each required broad gate once under its declared owner after focused checks
  pass, and rerun it only after a relevant change, an inconclusive infrastructure
  failure, or a repository-mandated second boundary.
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

## Context rollover

Treat context rollover as a coordinator lifecycle transition, not as worker
redispatch. Do not rely on a fixed token threshold unless the active product
surface explicitly exposes and guarantees one.

Prepare a rollover checkpoint when compaction is observed or expected, the
coordinator repeatedly reconstructs the same state, the initiative crosses a
major lifecycle boundary, or Codex surfaces a continuation or replacement task:

1. Stop new dispatches and freeze the current dashboard.
2. Write active outcome state, topology, agent paths or task IDs, branch/worktree
   ownership, implementation executor, immutable targets, blockers, decisions,
   and one next action to the durable tracker. Keep external conversation IDs in a
   private routing record when the durable tracker is public.
3. Record which workers are still running. Do not recreate, cancel, or adopt them
   solely because the UI shows another sidebar thread.
4. Build a compact coordinator handoff containing only authoritative locations,
   unresolved decisions, active routing IDs, and the next acceptance action.
5. Verify whether the new thread is a surfaced subagent, a continuation, or an
   independent user-owned task from its creation operation and lineage.
6. Let a successor coordinator adopt the durable checkpoint before it monitors,
   follows up, or dispatches anything. Reconcile live worker state once and avoid
   duplicate dispatch.

Compaction within the same thread does not itself create a new ownership boundary.
Create an independent coordinator task only when the product does so, the user
requests it, or separate lifecycle ownership is otherwise authorized and material.
Treat merge completion, a newly opened issue, a new authorization/risk boundary,
or a switch from delivery to extended maintenance as a positive rollover signal.
Reusing one coordinator is allowed, but it must not silently carry the prior
initiative's full working context into a materially new outcome.

## Delivery-to-Ops boundary

After delivery acceptance, classify the next action before continuing:

- Freeze the delivery outcome manifest, accepted immutable target, acceptance
  timestamp, elapsed-time cutoff, and the last available token counters before
  the first Ops action. Derive reported counts from the manifest and reconcile
  every commit, PR, or release identifier to one outcome row.

- Keep it in the current task only when it is a bounded recording or handoff action
  already authorized and uses the same risk boundary.
- Propose a separately tracked Ops outcome when work changes authorization, credentials,
  environment, tools, rollback needs, live-system risk, or monitoring duration—for
  example publication, merge, deployment, migration, or production observation.
- Do not dispatch the Ops outcome without explicit authorization. Choose a
  coordinator-owned subagent for bounded automation or an independent task when
  user-owned lifecycle is material. Give it a new compact dispatch packet,
  execution budget, durable state, and measurement boundary.
- Enumerate push, PR creation, merge, reconciliation, deployment, and cleanup
  separately. Do not widen a narrower action list announced in the current turn by
  later relying on standing policy; restate or request authorization first.
- If no Ops task is authorized, stop after recording the owner action and evidence.

When delivery and Ops remain in one user turn, preserve the cutoff anyway. Prefer
a context rollover before material deployment or migration when compaction has
occurred, the coordinator is reconstructing state, or the Ops packet is no longer
compact.


Start a new outcome when an Ops phase adds a new product or infrastructure change,
such as transport topology, account-provisioning mode, password policy, credential
rotation, or repository cleanup. Do not accumulate these changes under the title
and measurement boundary of the original feature delivery.
