# Reward-Hacking Audit

Reward hacking is not eliminated by having a verifier. Audit the environment as if an optimizing agent will search every exposed artifact, parser, path, and metric for shortcuts.

## Exploit Taxonomy
- Leakage / metadata exploitation: answers or decisive intermediate values are adjacent to the task.
- Tampering: agent can edit verifier code, tests, metrics, hidden labels, state, or imports.
- Sequence manipulation: agent can skip required upstream work and forge downstream artifacts.
- Proxy or parser gaming: shallow schema, default values, ambiguous formatting, self-reported metrics, or brittle parsers can pass.
- Special-casing visible checks: agent can branch on filenames, IDs, public tests, fixed seeds, or known examples.
- Denial of evaluation: agent can crash, timeout, exhaust resources, or break the grader.
- Evaluator bias/drift: LLM judge or reward model is sensitive to style, length, model family, or distribution shift.
- Internal-channel leakage: messages, scratchpads, memory, tool args, logs, or shared stores leak answers or private criteria.

## Hardening Checklist
- Keep evaluator code, hidden labels, held-out tests, and scoring scripts outside agent-writeable paths.
- Do not place private policies, rubrics, answer-bearing metadata, grader internals, hidden docs, or verifier secrets under an agent-readable task root.
- Use read-only mounts or equivalent protection for evaluator-relevant files.
- Remove task-adjacent metadata from the agent workspace.
- Use strict schemas and fail-closed parsing.
- Recompute dependencies from upstream artifacts instead of trusting submitted markers.
- Randomize intermediate outputs or seeds when possible.
- Add hidden/adversarial/isomorphic variants.
- Add canaries for train/eval leakage and internal-channel leakage.
- Log file reads/writes, tool calls, environment mutations, and grader discrepancies.
- Report task success separately from integrity-clean success and unsafe-action rate.

## Verifier Robustness
- Test full response versus extracted answer.
- Test short versus long responses.
- Test equivalent prompt rewrites and isomorphic task variants.
- Test hidden splits and adversarial variants.
- Calibrate LLM judges or learned rewards against expert/gold labels.
- Plot proxy reward versus ground-truth/task-quality signal during optimization.

## Training Stop Signals
- Proxy reward rises while gold success or integrity-clean success stalls/falls.
- Exploit rate is nonzero on high-severity paths.
- Unsafe-action rate increases with task success.
- Unsafe-but-passing action rate is nonzero for financial, customer-support, legal, medical, infrastructure, or security environments.
- Reward variance collapses for group-normalized RL.
- A policy discovers a new exploit category not covered by the audit.
