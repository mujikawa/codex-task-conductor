# Parallel readiness gate

Use serial dispatch by default. Require every check to pass before parallel dispatch.

## Terminology

- **Concurrency:** tasks are active during overlapping time windows; execution may be interleaved.
- **Parallelism:** workers actually execute at the same instant.

The coordinator controls concurrency. The execution platform determines actual parallelism. Do not infer parallel execution from dispatch alone.

## Authorization and limit

- Obtain explicit current authorization for the exact concurrency.
- Use at most two mutating workers for the first parallel pilot.
- Do not treat a prior pilot, tracker, or this skill as standing parallel authorization.

## Required checks

| Check | Pass condition |
| --- | --- |
| Independent outcome | Each task has stable scope and an independently verifiable Definition of Done. |
| Dependency graph | No dispatched task requires another active worker's output or decision. |
| Frozen contract | Shared APIs, schemas, types, fixtures, and interfaces are fixed. |
| Mutation scope | Workers do not modify the same files, objects, migrations, generated artifacts, or shared configuration. |
| Git isolation | Each mutating worker has a dedicated branch and worktree from a pinned base. |
| Resource isolation | Workers do not share a mutable database, port, deployment environment, lockfile operation, credential, or exclusive service resource. |
| Integration plan | Merge order, conflict owner, and post-integration gate are defined. |
| Acceptance capacity | The coordinator can independently verify every worker. |
| Execution budget | Execution profiles and the combined token/latency tradeoff are recorded and acceptable. |
| Authorization boundary | Production, deployment, credentials, destructive actions, and owner-only operations remain bounded. |

Record every result. Do not replace the table with a general claim that tasks look independent.

## Do not parallelize

- unresolved requirements or architecture decisions
- outcomes where one worker defines another worker's input
- the same branch, worktree, source files, migration chain, schema objects, or generated artifacts
- production or deployment operations sharing one environment
- work depending on mutable external state without isolation
- tasks likely to require repeated cross-worker clarification or conflict resolution

## Failure behavior

- Keep independent workers running when an unrelated outcome fails.
- Pause dependent workers when a prerequisite fails or changes.
- Stop the batch when a shared contract, base, resource, or authorization boundary drifts.
- Convert material scope changes into new tracked outcomes.

## Acceptance

1. **Individual acceptance:** verify each worker's repository, branch, worktree, HEAD, diff, tests, and Definition of Done.
2. **Integration acceptance:** combine accepted outcomes in the declared order and run the shared gate.

Accept the initiative only after both gates pass.
