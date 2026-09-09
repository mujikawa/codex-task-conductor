# Task Conductor v0.1.8-preview

Repeated worker handoffs can omit evidence or report checks against a different
candidate. This release adds an optional JSON completion receipt and a Python
standard-library validator that detects missing fields and inconsistent candidate
claims. It does not verify evidence truth or grant acceptance.

Evidence reuse now explicitly depends on the immutable target, relevant inputs,
gate configuration, and environment. Failure guidance distinguishes missing
receipt data, behavioral failures, uncertain execution, and authority boundaries.
No workflow engine, automatic cache, or additional retry budget is introduced.

Validation: four offline regression test groups covering receipt contracts and
CLI behavior, official skill validation, local Markdown links, and diff checks.
No new live-agent pilot or efficiency improvement is claimed.
