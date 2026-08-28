# Field observation: cost-aware AGY orchestration

## Status and publication boundary

This anonymized field observation combines two Windows delivery workflows. It is
published as a process case, not a repository walkthrough, product disclosure, or
cost benchmark. Task, conversation, repository, issue, pull-request, account,
host, and absolute filesystem identifiers are intentionally omitted.

AGY and Codex report different usage counters and have different pricing. The user
selected an AGY hard cap of 10 loops because AGY tokens were economically cheaper
for this workload. The observation therefore preserves that choice and evaluates
whether each loop converged; it does not assume that a smaller numeric cap is
always better.

## Delivery shapes

| Shape | Topology | AGY execution | Result |
| --- | --- | --- | --- |
| A | One coordinator plus one coordinator-owned Codex worker | One AGY implementation invocation, followed by independent Codex review and correction | Accepted |
| B | One coordinator plus four serial coordinator-owned Codex workers, then coordinator integration | 23 observed AGY loops across four outcomes; one outcome reached the authorized cap of 10 before Codex catch-up | Accepted initiative |
| B follow-on | Same long coordinator, new bounded outcome | Coordinator invoked AGY directly twice instead of dispatching a fresh worker | Delivered, but with a weaker ownership and context boundary |

The outcomes differed in scope and cannot be compared as equivalent units.

## What worked

- Coordinator-owned workers were easier to automate and monitor than independent
  user-owned tasks for bounded implementation.
- Dedicated branches and linked worktrees preserved single-writer ownership and
  made the coordinator's acceptance target reviewable.
- AGY performed substantial implementation at the deliberately lower-cost
  executor layer; Codex independently found semantic, portability, security, and
  transaction-boundary defects that executor success alone did not establish.
- Serial execution was appropriate where generated contracts, shared styles, or
  integration gates overlapped.
- Retaining durable scope and evidence allowed the coordinator to integrate
  multiple immutable outcomes without accepting worker summaries as proof.

## Friction and adaptations

### Compact dispatch instead of full-history inheritance

One bounded worker inherited the coordinator's complete history. Most reported
Codex input was cached, but the large repeated prefix still accumulated across
cycles. Future workers receive a compact outcome packet and no inherited history,
or the smallest recent slice needed to carry trusted user authorization.

### Receipt retention through the candidate gate

Early serial outcomes removed the private AGY receipt after focused checks. Later
lint or end-of-file findings then lacked the receipt-bound route needed for legal
same-conversation remediation. A later outcome retained the receipt until the
immutable candidate and broad gate passed. The receipt stays private and outside
the accepted commit, but remains available until acceptance is frozen.

### Runtime ownership before delegation

Large ignored dependency and environment trees repeatedly blocked clean-baseline
validation. The improved packet declares who owns environments, dependency trees,
caches, and generated outputs; whether AGY should run before they are created; and
the exact cleanup envelope, if the user authorizes one. A worktree environment is
not deleted or rebuilt merely to satisfy automation cleanliness.

### Unsupported structural operations

AGY's permitted editing tools could not reliably delete tracked files and instead
left empty placeholders. Once an operation is known to be unsupported, it is
routed back to Codex under the existing authorization boundary. Repeating the same
AGY attempt is not convergence.

### Economic cap plus convergence checkpoint

The 10-loop hard cap remains valid because it reflects the user's executor-cost
preference. It is paired with an evidence checkpoint after every loop:

- continue when a new review finding is addressed, the diff materially improves,
  or a verification result moves toward the frozen gate;
- stop early on the same unchanged failure, no net diff, unsupported operation,
  deterministic infrastructure failure, scope drift, new authority, or exhausted
  cap;
- record product remediation, verification remediation, transient retry, and
  Codex catch-up separately.

For future runs, each real invocation that preserves wrapper control files records
AGY's conversation-cumulative usage and a per-invocation delta. This prevents
same-conversation remediation from double-counting earlier turns. Cache hits and
policy rejections before AGY starts do not create AGY usage attempts.

This preserves inexpensive iteration without turning 10 into a target that must be
consumed.

When AGY determines that a remaining operation is beyond its capabilities or
permitted tools, it should hand off immediately rather than consume the remaining
budget. The handoff preserves the baseline, actual diff, completed criteria,
remaining gap, unavailable operation, validation evidence, and one next Codex
action. Codex then finishes only the already authorized scope and reviews the
combined result. The observed Codex catch-up followed this executor-handoff shape.

### Rollover at a material lifecycle boundary

After a multi-outcome initiative completed, the same long coordinator adopted a
new issue and invoked AGY directly. The work remained isolated, but the topology
changed and accumulated context continued. Merge completion, a new issue, or a new
risk boundary should trigger a durable checkpoint and compact coordinator
rollover, even when the product permits continuing in the same task.

## Observed telemetry

| Boundary | Codex reported tokens | AGY reported usage | Wall-clock window | Notes |
| --- | ---: | ---: | ---: | --- |
| Shape A | about 30.6M core plus 1.5M automatic review | about 0.85M for one invocation | about 61 minutes | One coordinator, one worker, one compaction |
| Shape B | about 84.4M core plus 1.8M automatic review | 23 loops; complete aggregate unavailable | about 6h 37m | Four serial workers plus integration, two compactions |
| Shape B follow-on | about 42.0M core plus 0.7M automatic review | Two invocations; complete aggregate unavailable | about 1h 38m | New outcome reused the long coordinator |

Approximately 98% of observed Codex input was cached in these workflows. Cached
input is still cumulative repeated processing, not a count of unique content and
not proof that a cycle was free. AGY counters are shown separately because their
token definitions and pricing are not normalized with Codex. Scope, validation,
and lifecycle differences prevent savings percentages or causal comparisons.

## Public-share checklist

Publish the implementation method and adaptations, not private routing data:

- omit raw Codex task IDs, AGY conversation IDs, absolute paths, account details,
  credentials, production data, customer names, and private URLs;
- generalize repository, issue, and product names unless they are intentionally
  public and necessary to reproduce the lesson;
- identify observation dates, topology, acceptance boundary, missing telemetry,
  and whether counters are cumulative or per invocation;
- distinguish executor success from Codex acceptance and observed cost from a
  controlled benchmark;
- disclose failures and corrections so the case is useful rather than promotional.

## Adopted conclusion

The useful control is not a universally small AGY loop count. It is a declared
economic ceiling, evidence of convergence on every loop, immediate capability
handoff when appropriate, independent Codex acceptance, and a clean lifecycle
boundary before the next outcome. This keeps the lower-cost executor available for
iterative work without hiding coordination, review, or context costs.
