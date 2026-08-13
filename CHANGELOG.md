# Changelog

All notable changes to Task Conductor will be documented in this file.

## Unreleased

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
- Correction envelopes, layered tracker guidance, stable review-target rules,
  worktree cleanup classification, Windows host preflight, and production rehearsal
  requirements.

### Changed

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
