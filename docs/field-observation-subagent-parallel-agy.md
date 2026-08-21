# Field observation: subagent-first, controlled concurrency, and AGY recovery boundaries

## Status

Forward clean-room observation recorded on 2026-08-20 and updated with the
authorized 2026-08-21 recovery attempt from an isolated local Git fixture on
Windows. Account, session, routing, and absolute filesystem identifiers are
intentionally omitted. No product repository source, remote, pull request,
deployment, or cleanup was mutated by the pilots.

The observation contains four bounded outcomes:

| Outcome | Topology | Result |
| --- | --- | --- |
| Serial direct | Coordinator plus one coordinator-owned Codex worker | Accepted |
| Serial AGY | Coordinator plus one coordinator-owned Codex worker managing AGY | `needs_followup`; final fresh `SUCCESS` still failed the exact LF-byte contract |
| Portable-EOL serial AGY | Coordinator plus serial replacement workers managing AGY | Accepted after one zero-change service retry |
| Two-worker concurrent | Coordinator plus two isolated coordinator-owned Codex workers | Accepted after ordered integration |

These outcomes validate workflow boundaries, not token savings or elapsed-time
improvement. The concurrent pilot proves controlled overlap and integration
acceptance; it does not prove hardware-level simultaneous model execution.

## Frozen fixture contract

The original serial direct, original serial AGY, and parallel outcomes started
from commit `4a428154d71d73ac99d5f1a65697f827ea6ebde3`. The portable-EOL outcome
started from descendant commit `18152cc08922635e195aabba521895fe6510e81c`,
which added the repository-owned LF policy and its tracker contract. Each
mutating worker owned a dedicated branch, physical worktree, and one exact file.
The coordinator owned acceptance and integration. Commits, pushes, pull
requests, deployments, external tracker changes, and cleanup were outside worker
scope.

The parallel readiness gate passed before dispatch: outcomes and dependencies
were explicit, the base and contracts were frozen, mutation paths and runtime
resources did not overlap, integration order was A then B, the coordinator had
acceptance capacity, execution profiles were bounded, and no production,
credential, or external side effect was involved.

## Serial direct result

The direct Codex worker returned immutable commit
`c7701ff238e0a59c2924654454b29ed1eeae8150`. It changed only the assigned serial
marker. The coordinator independently verified base ancestry, the sole changed
path, whitespace checks, the exact committed content, and a clean worktree before
acceptance.

One Windows fixture worktree triggered Git's dubious-ownership protection. The
worker used command-scoped `safe.directory` configuration only. It did not modify
global Git configuration or weaken repository policy.

## Controlled two-worker result

Worker A returned commit
`d6a4bac480f5490013d2a294bef446f012011f6c`; worker B returned
`b4b4a00d8093bf84e307a2a76444353d4d0ae99b`. Each commit descended directly from
the frozen base and changed only its assigned file. The coordinator independently
accepted both candidates.

Worker B initially stopped because the clean Windows checkout materialized the
fixture's initial text with CRLF while the packet described a final LF byte
contract. The coordinator clarified the same frozen outcome: initial checkout
materialization was allowed, final committed content was unchanged, and no
repository-wide normalization was authorized. The original worker then completed
the same outcome with one clarification and no scope expansion.

The coordinator integrated A then B into immutable commit
`a79953c9cb326f1bf6cd6e8b01f3d0ddcf863a7e`. Independent acceptance verified two
ordered commits, exactly the two assigned paths, exact LF Git blobs, unchanged
unassigned blobs, whitespace checks, and a clean integration worktree. A fresh
Windows checkout again materialized text as CRLF. This shows that portable byte
contracts should verify committed blobs or freeze EOL behavior with
`.gitattributes`; worktree bytes alone are not portable evidence.

## AGY result

The AGY worker verified the AGY executable and version, canonical repository and
branch, pinned base, ancestry, baseline cleanliness, and baseline diff checks. It
then invoked the separately installed `$delegate-to-agy` wrapper exactly once.

The first invocation stopped during the wrapper's Git change inspection before
AGY started. The installed wrapper matched its separately maintained source, so
installation drift was ruled out. Follow-up diagnosis showed that the linked
worktree had been created under the sandbox identity while the approved wrapper
ran under the host identity. Standalone Git checks run inside the sandbox passed;
host Git rejected the differently owned worktree.

A separately authorized maintenance outcome added command-scoped
`safe.directory` only for the canonical workspace already derived and validated
by the wrapper. It did not change global Git configuration or AGY permissions.
The repair passed the original validation-only reproduction, PowerShell parsing,
the official skill validator, and rule preview. Commit
`4b2ba221a9273e0c2c5fc066167824fc28b81f4b` was published to the separately
maintained skill repository. The reinstalled skill matched all 11 published Git
blobs and passed the original task's installed-wrapper validation.

The same Codex worker then continued the frozen outcome. AGY 1.1.16 launched in a
fresh conversation but returned terminal status `ERROR` after its sandbox denied
an attempted PowerShell byte-check command. It left only the allowed marker file
changed. Independent Codex review found logical text `agy-pass` but bytes ending
in CRLF rather than the required LF. There was no receipt or commit. The private
conversation ID is intentionally omitted.

Because a failed AGY run left a tracked partial change, the worker correctly did
not start the one otherwise permitted fresh retry. It also did not relabel the
partial output, normalize the line ending, or commit it. The outcome remains
`needs_followup` pending explicit authority to restore the single file to the
pinned base and begin another fresh implementation attempt.

After explicit recovery authorization, the coordinator restored the single
partial file to the pinned base and clarified the same task without changing its
scope or Definition of Done. AGY was told to use only its workspace edit tool;
Codex retained responsibility for exact-byte verification. Installed-wrapper
validation passed with no cache hit. AGY 1.1.17 then returned `SUCCESS` in a new
conversation and changed only the allowed file, but Codex again measured CRLF
instead of LF.

The worker converted the private task into a same-conversation remediation packet
for that concrete finding. The wrapper rejected it before AGY started because its
clean-baseline exception admits allowed dirty output only when the receipt matches
the current task hash. A successful implementation receipt binds the prior
implementation task, while a remediation packet necessarily has a different hash.
The task and receipt carried the same private conversation ID, but that valid
routing relationship was not considered by the baseline exception. No AGY
remediation pass or commit occurred.

A second authorized wrapper maintenance outcome implemented that boundary. It
admits receipt-bound remediation only when receipt status, prior task SHA format,
conversation identity, current output hashes, and current write scope all agree.
The real blocked packet passed validation as a non-cache remediation baseline.
Commit `d03fd77f1d1b38a6f94028aea54567d27efceb8c` was published, reinstalled, and
matched all 11 published Git blobs.

The same worker then invoked exactly one remediation against the existing private
conversation. AGY 1.1.17 changed the file to the correct nine LF-terminated bytes,
but returned terminal `ERROR`: a later fuzzy fallback reported no net diff and
could not find the old target content. Codex independently verified the correct
artifact, sole changed path, and whitespace gate. The prior receipt was not
replaced because the remediation did not return `SUCCESS`. The frozen contract
therefore prohibited a commit or acceptance even though the artifact itself was
correct.

For one final bounded attempt, the coordinator retained that evidence, restored
the sole tracked file to the pinned base, and created a fresh implementation task
with a null conversation ID. Installed-wrapper validation passed with one write
path, no cache hit, and no remediation baseline. AGY 1.1.17 returned `SUCCESS` in
one turn and produced a current receipt that correctly bound the fresh task and
the actual output. Codex independently found only the allowed file changed and a
clean whitespace check, but the worktree again contained 10-byte CRLF
`6167792D706173730D0A`, not the required 9-byte LF
`6167792D706173730A`. The worker obeyed the no-retry boundary and created no
commit. The private conversation ID remains omitted.

A separate coordinator acceptance command also demonstrated that an unquoted
revision expression constructed as `$base..$head` is not a reliable Git argument.
The durable rule is to validate the actual execution identity, workspace
ownership, and external-process invocation path rather than relying on an
equivalent command run in a different context.

## Portable-EOL AGY result

The old exact-worktree-byte outcome remained unaccepted. A newly scoped pilot
instead committed `src/*.txt text eol=lf` in `.gitattributes` and declared the
immutable Git blob as the portable byte boundary. A new pinned base and linked
worktree materialized the initial marker with LF before dispatch.

The first worker was created before the trusted user authorization for external
AGY disclosure. Its wrapper launch and one coordinator-relayed follow-up were both
stopped before process creation because assistant relay text was not accepted as
trusted user authorization. No AGY invocation was consumed. The user then
explicitly authorized a replacement worker that directly inherited the message.
Its fresh AGY call ended at eligibility check with `503 UNAVAILABLE`, zero turns,
zero tokens, no conversation, no receipt, and no workspace change.

Because the failed executor call left no changes, the delegation contract allowed
one fresh retry. A separately authorized retry replacement directly inherited the
new trusted message. AGY 1.1.17 returned terminal `SUCCESS` in one turn, and its
current receipt bound both the fresh task and actual output. The worker committed
only `src/agy.txt` as
`57202c365a2fc22721989605da9a8de6d3337a3f`. Independent coordinator acceptance
verified pinned-base ancestry, exact scope, no `.agy` artifact, clean whitespace
and tracked state, blob `8fa3b154de706ac4bf672151e0d9c97a74358cdb`, size 9,
and exact committed bytes `6167792D706173730A`. The outcome was accepted; branch
and worktree cleanup remained outside authorization.

## Measurement

Worker token counters and active model time were unavailable and are not
estimated. Observable execution counts were:

- serial direct: one worker delivery and one independent coordinator acceptance;
- parallel A: one worker delivery and one independent coordinator acceptance;
- parallel B: one initial stop, one same-outcome clarification, one delivery, and
  one independent coordinator acceptance;
- integration: one ordered A-then-B integration and one independent acceptance;
- AGY first stage: one implementation-wrapper attempt, one read-only validation
  diagnosis, zero AGY launches, zero remediation passes, and zero commits;
- wrapper maintenance: one focused correction, one publication cycle, one
  reinstall, and one installed-copy validation;
- AGY follow-up: one fresh AGY launch, zero retries, zero remediation passes, and
  zero commits. AGY reported 47,613 input, 1,305 output, and 979 thinking tokens
  over 11.614 seconds; Codex token and active-time telemetry were unavailable.
- second AGY follow-up: one authorized restore, one task clarification, one fresh
  AGY `SUCCESS`, one wrapper-level remediation rejection, zero completed
  remediation passes, and zero commits. AGY reported 66,504 input, 3,762 output,
  and 3,004 thinking tokens, including 52,839 cache-read tokens, over 19.587
  seconds; Codex token and active-time telemetry were unavailable.
- second wrapper maintenance: one focused correction, one publication cycle, one
  reinstall, and one exact receipt-bound remediation validation;
- third AGY follow-up: one same-conversation remediation invocation, terminal
  `ERROR`, zero successful remediation passes, and zero commits. AGY reported
  103,282 input, 6,409 output, and 4,998 thinking tokens, including 130,593
  cache-read tokens, over 820.063 seconds and two turns. Codex token and
  active-time telemetry were unavailable.
- fourth AGY follow-up: one authorized restore, one validated fresh task, one AGY
  `SUCCESS`, zero retries, zero remediation passes, and zero commits. AGY reported
  50,170 input, 4,000 output, and 3,661 thinking tokens, with zero cache-read
  tokens, over 15.779 seconds and one turn. The wrapper wait was approximately
  37.5 seconds; Codex token and active-time telemetry were unavailable.
- portable-EOL setup and authorization recovery: one local pinned-base commit,
  one fresh linked worktree, three serial worker roots, and two wrapper launches
  rejected before AGY process creation because trusted authorization was not
  directly inherited. No concurrent writer existed.
- portable-EOL AGY execution: one actual fresh invocation failed with service
  `503 UNAVAILABLE`, zero turns, zero tokens, and no changes; the single permitted
  fresh retry returned `SUCCESS`, produced one immutable worker commit, and passed
  one independent coordinator acceptance. The successful retry reported 41,359
  input, 1,895 output, 1,465 thinking, and 24,409 cache-read tokens, 43,254 total,
  over 11.010 seconds and one turn. Product corrections and remediation were zero;
  Codex token and active-time telemetry were unavailable.

Elapsed wall-clock would mix coordinator work, tool execution, approval waiting,
and concurrent workers, so this observation does not publish it as active work.

## Lessons adopted

1. Coordinator-owned subagents can complete bounded delivery and acceptance
   without creating user-owned sidebar tasks.
2. Controlled concurrency needs a frozen readiness record and an explicit ordered
   integration gate; worker success summaries are insufficient.
3. Same-outcome clarification is appropriate when the packet is ambiguous but the
   outcome, allowed paths, base, and acceptance contract remain unchanged.
4. Exact text-byte contracts must distinguish committed blobs from platform
   checkout materialization.
5. External wrappers need validation under the same execution identity and
   ownership boundary used in production. Equivalent sandbox commands do not
   prove a host invocation is sound.
6. A failed executor run with a partial change must remain `needs_followup`; it
   cannot be normalized, retried, or counted as success without the authority
   required by the delegation contract.
7. A remediation receipt contract must distinguish an unchanged cached rerun from
   a new remediation task. Conversation identity, prior receipt integrity,
   current output hashes, and current write scope must all agree before admitting
   dirty baseline output.
8. Correct artifacts from a terminally failed executor run remain review evidence,
   not successful execution evidence. A wrapper must not synthesize `SUCCESS` or
   refresh the receipt merely because post-run inspection likes the result.
9. Executor prose, terminal `SUCCESS`, and a valid receipt do not prove an exact
   byte contract. On Windows, use repository-owned EOL policy such as
   `.gitattributes` or define acceptance against committed blobs when that is the
   intended portability boundary; otherwise independently inspect raw worktree
   bytes and keep a mismatch unaccepted.
10. External-delegation authorization must be directly visible as trusted user
    input to the worker whose policy engine launches the executor. Coordinator
    relay text is a routing aid, not a substitute for that trust boundary; create
    a newly authorized replacement rather than bypassing the policy in the
    coordinator.
