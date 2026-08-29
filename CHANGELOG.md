# Changelog

All notable changes to Task Conductor will be documented in this file.

## 0.1.3-preview - 2026-08-29

### Changed

- Worker dispatch now records the smallest trusted-context inheritance needed for
  authorization instead of treating full-history inheritance as a convenience.
- Validation is assigned across objective-specific worker probes, one immutable-
  candidate broad gate, and one integration gate, with duplicate broad runs
  requiring an explicit reason.
- AGY packets now declare final output shape, validation-only preflight, semantic
  no-op and structural probes, and remediation-before-runtime sequencing.

## 0.1.2-preview - 2026-08-29

### Added

- An anonymized public field observation of cost-aware AGY delegation across one
  bounded worker and a four-outcome serial initiative.

### Changed

- AGY cycle guidance now separates an economics-based hard cap from evidence-based
  convergence checkpoints instead of treating every higher cap as excess, and
  defines immediate capability handoff to Codex before the cap is exhausted.
- Dispatch packets now retain successful receipts through immutable candidate
  acceptance, declare runtime-artifact ownership and structural-operation limits,
  and avoid full-history inheritance unless needed for trusted authorization.
- Measurement now reports AGY and Codex usage separately, records loop categories
  and cost rationale, uses receipt-based per-invocation deltas without recounting
  cumulative conversations, and treats lifecycle rollover as a first-class boundary.

## 0.1.1-preview - 2026-08-21

### Added

- A clean-room field observation covering one accepted coordinator-owned direct
  worker, a controlled two-worker integration, and AGY wrapper and executor
  failure boundaries.

### Changed

- Recorded the first passing subagent-first serial pilot, controlled two-worker
  concurrent pilot, and accepted portable-EOL AGY pilot. The AGY case preserves
  the earlier wrapper, terminal-status, receipt, Windows worktree-byte,
  trusted-authorization, and service-retry failures instead of collapsing them
  into the final success.

## 0.1.0-preview - 2026-08-20

### Added

- Bounded coordinator and worker contracts.
- Dedicated branch and worktree isolation guidance.
- Parallel readiness, execution-profile, measurement, and evidence-based acceptance rules.
- Repository adoption guide and task-governance template.
- First serial operational baseline with an explicit telemetry cutoff.
- Second serial case study covering one independent worker, one independent reviewer, acceptance, Git lifecycle, and deployment with separate measurement boundaries.
- Content-loading profiles for both serial pilots, including cache ratios, uncached input, cycle proxies, context peaks, compaction, and retained-telemetry limits.
- Release checklist and clean-room verification procedure.
- Dispatch troubleshooting for destination ambiguity, bounded task inventory, ownership proof, and topology drift.
- Compact dispatch and acceptance packets, context and review-readiness gates,
  model/tool cycle budgets, and bounded input-reduction rules.
- A delivery-to-Ops decision boundary and Pilot 3 observational validation metrics.
- A retrospective long-lifecycle field observation with phase cutoffs and
  lower-bound telemetry handling for missing root logs.
- A zero-dispatch manual-serial field observation with complete single-root
  telemetry, topology audit, delivery cutoff, and context-loading profile.
- An independent serial-pilot field observation covering a post-merge gate escape,
  runtime-ownership incidents, publication authorization wording, and separated
  product/recovery/review/publication accounting.
- Correction envelopes, layered tracker guidance, stable review-target rules,
  worktree cleanup classification, Windows host preflight, and production rehearsal
  requirements.

### Changed

- Coordinator-owned subagents are now the preferred bounded automation topology;
  independent user-owned tasks are reserved for material lifecycle boundaries.
- Added a durable context-rollover protocol that distinguishes compaction,
  surfaced subagent threads, and independent coordinator tasks while preventing
  duplicate dispatch.
- Added an optional `$delegate-to-agy` executor contract that keeps Codex worker
  ownership separate from external implementation, requires clean linked
  worktrees and one writer, and leaves the AGY wrapper under its own skill.
- Candidate gates must now pass on the immutable single-worker target before formal
  acceptance; merged-only gates keep lifecycle at `integrating`. Runtime-resource
  ownership and publication side effects must be enumerated explicitly.
- Independent task creation failures now stop the workflow instead of silently falling back to a background subagent.
- Measurement guidance now separates completed, accepted, and follow-up outcomes and classifies topology from creation evidence.
- Measurement guidance now preserves the delivery-acceptance cutoff when later Git lifecycle or deployment work continues in the same coordinator.
- Measurement guidance now distinguishes cumulative input from unique content and prohibits extrapolating per-call context metrics from missing task logs.
- Ownership inventory failures now resolve to `unknown` and require corroboration from known task IDs, Git state, and durable tracking.
- Explicit destination binding can resume dispatch without metadata cleanup after fresh mapping and ownership checks pass.
- A client-side creation handle is now recorded as `creation accepted / formal ID unresolved / execution unknown`; recent-inventory absence is no longer described as pending setup or a worker that has not started.
- Material feature, infrastructure, credential, policy, deployment, and cleanup
  expansion now creates a new tracked outcome and measurement boundary instead of
  silently extending the original delivery.
