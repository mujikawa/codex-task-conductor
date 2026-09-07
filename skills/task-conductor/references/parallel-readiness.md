# Parallel readiness gate

Use serial mutation by default. For authorized parallel work, apply each check to
the resources and operations the workers actually use. Read-only work does not
require a new branch, worktree, or merge plan when it can inspect a stable target
without changing shared state. A command that writes caches or generated output
is not read-only merely because it is called a check.

## Terminology

- **Concurrency:** tasks are active during overlapping time windows; execution may be interleaved.
- **Parallelism:** workers actually execute at the same instant.

The coordinator controls concurrency. The execution platform determines actual parallelism. Do not infer parallel execution from dispatch alone.

## Authorization and limit

- Verify existing authorization and stay within its concurrency limit. Do not
  request fresh permission for each batch within the same scope and limit.
- Use at most two mutating workers for the first parallel pilot.
- A prior pilot, tracker, or this skill alone is not authorization. Preserve an
  explicit standing authorization within its stated boundary.

## Required checks

| Check | Pass condition |
| --- | --- |
| Independent outcome | Each task has stable scope and an independently verifiable Definition of Done. |
| Dependency graph | No dispatched task requires another active worker's output or decision. |
| Frozen contract | Shared APIs, schemas, types, fixtures, and interfaces are fixed. |
| Mutation scope | Workers do not modify the same files, objects, migrations, generated artifacts, or shared configuration. |
| Git isolation (mutation only) | Each mutating worker has a dedicated branch and worktree from a pinned base. |
| Resource isolation | Workers do not share a mutable database, port, deployment environment, lockfile operation, credential, or exclusive service resource. |
| Integration plan (combined changes only) | Merge order, conflict owner, and post-integration gate are defined. |
| Acceptance capacity | The coordinator can independently verify every worker. |
| Execution profile | Model inheritance or authorized overrides are recorded; any explicit resource limits are respected. No default cycle budget is required. |
| Authorization boundary | Production, deployment, credentials, destructive actions, and owner-only operations remain bounded. |

Record applicable results and mark mutation-only checks not applicable for read-only work. Do not replace the table with a general claim that tasks look independent.

## Do not parallelize

- unresolved requirements or architecture decisions
- outcomes where one worker defines another worker's input
- concurrent writes to the same branch, worktree, source files, migration chain, schema objects, or generated artifacts
- production or deployment operations sharing one environment
- work depending on mutable external state without isolation
- tasks likely to require repeated cross-worker clarification or conflict resolution

## Failure behavior

- Keep unaffected workers running when an unrelated outcome fails.
- Pause dependent workers when a prerequisite fails or changes.
- Stop the batch when a shared contract, base, resource, or authorization boundary drifts.
- Convert material scope changes into new tracked outcomes.

## Acceptance

1. **Individual acceptance:** verify each worker's target and Definition of Done evidence; for mutating work also verify branch, worktree, HEAD, diff, and required tests.
2. **Integration acceptance:** combine accepted outcomes in the declared order and run the shared gate.

For outcomes that combine changes, accept the initiative only after both gates
pass. Read-only analysis requires individual evidence acceptance but no synthetic
merge or integration test.
