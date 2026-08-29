# Task Conductor v0.1.4-preview

This preview turns a nine-outcome autonomous release observation into four durable
controls: verified authorization anchors, reconciled outcome manifests, a frozen
Delivery-to-Ops cutoff, and one optional integrated reviewer for high-risk releases.

## Highlights

- Worker context selection records and verifies the trusted authorization-bearing
  user turn; a fixed turn count alone is insufficient.
- Worker, commit, PR, accepted, and deployed counts derive from one durable outcome
  manifest and reconcile to published identifiers.
- Delivery freezes its accepted target, manifest, timestamp, and token counters
  before publication, migration, deployment, or live operation.
- External-delegation approval rejection before process creation is recorded as a
  zero-invocation boundary event and can hand off to Codex without a retry loop.
- A multi-outcome production release may use one final read-only integrated
  reviewer when risk warrants it, without repeating broad gates by default.

## Install

```text
Use $skill-installer to install skills/task-conductor from
mujikawa/codex-task-conductor at ref v0.1.4-preview.
```

`$delegate-to-agy` remains an optional separately installed dependency. Use its
matching v0.1.4 release for the updated disclosure and handoff reporting contract.

## Release status

This remains a preview. The field observation validates autonomous bounded
delivery and safety boundaries, not controlled token savings or universal
production reliability.
