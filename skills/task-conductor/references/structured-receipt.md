# Optional structured worker receipt

Use a JSON receipt when repeated dispatches or automated collection make missing
evidence costly. Ordinary bounded work may use the existing prose contract.
Agree on this format before dispatch; do not request a second narrative copy.

Run with an available Python 3 runtime (standard library only):

```text
python <installed-skill>/scripts/validate_receipt.py <receipt.json>
```

Exit 0 means the record has valid shape and internally consistent candidate
claims; exit 1 reports errors as JSON. Neither means acceptance. The validator
does not execute commands, inspect Git, open evidence links, or verify that the
declared checks exhaust the frozen gate. The coordinator still verifies these.

Version 1 fields:

| Fields | Value |
| --- | --- |
| `version` | Integer `1` |
| `state` | `candidate` or `incomplete`; never worker-declared `accepted` |
| `outcome`, `tracker` | Bounded outcome and canonical durable record |
| `worker`, `topology`, `routing_id` | Title, observed topology, transient routing identifier |
| `executor`, `execution_profile` | Executor and selected settings or `default/inherited` |
| `repository`, `branch`, `worktree`, `base`, `target` | Repository identity and immutable target; use `none` or `unavailable` where genuinely inapplicable |
| `rationale`, `next_action` | Change rationale and one next action |
| `changed_files`, `risks`, `blockers`, `owner_actions` | Arrays of nonempty strings; empty arrays explicitly mean none |
| `checks` | Array of objects with `command`, `result`, `evidence`, `target` |
| `dod` | Array of objects with `criterion`, `result`, `evidence` |
| `telemetry` | Object with `tokens` and `elapsed_seconds`: nonnegative numbers or `null` for unavailable |

All textual fields are nonempty strings. Results are `pass`, `fail`, or `not-run`.
A candidate needs nonempty checks and DoD evidence, all passing, checks bound to
the candidate target, and no blockers. This state means ready for coordinator
inspection, not accepted. If an integrated gate remains pending, use `incomplete`
and identify its owner and next action; the immutable target can still be supplied.
Record scoped omissions and approved exemptions in the evidence rather than
inventing successful test results. Additional fields may retain executor-specific
details, including the existing AGY completion requirements; they are not validated.

Keep private routing, logs, and executor details in authorized runtime storage.
Link a compact, sanitized evidence index from the canonical tracker. Generate
summaries from the receipt; do not create another authoritative status database.

## Evidence reuse and continuation

Reuse evidence only while its immutable target, relevant inputs, gate configuration,
and environment remain applicable. Prompt equality, working-directory equality,
or a successful process exit is insufficient. Reconcile live worker ownership,
Git, PR, and external state before continuing. Do not replay publication or other
side effects from cached success; verify their actual result before any retry.
No automatic cache or workflow runner is introduced by this receipt format.

## Failure handling

| Failure | Next action |
| --- | --- |
| Missing or malformed receipt fields | Request only the missing/corrected evidence; do not rerun implementation automatically |
| Failed behavioral check | Correct within authorized scope, then rerun affected required gates on the new target |
| Executor launch or transient transport failure | Verify whether execution or mutation occurred before applying that executor's retry policy |
| Timeout or lost connection after dispatch | Reconcile process, worker, and repository state; do not assume zero side effects |
| Authorization denial, cancellation, invalid configuration | Resolve the cause or stop dependent work; never retry unchanged or widen permissions |

Preserve explicit hard limits and external-executor policies. Do not add universal
round limits or bypass isolation, authorization, and independent acceptance.
