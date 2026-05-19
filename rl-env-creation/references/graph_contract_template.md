# Environment Contract Template

Use this as the source of truth for a hand-crafted, generated, or hybrid RL environment. Every accepted task must be traceable to this contract.

## 1) Capability Axis
- Primary axis: tool use, planning, adaptability, groundedness, domain reasoning, recovery, safety/authorization, or other.
- Secondary axes, if any.
- Failure taxonomy used for diagnosis.
- Stakeholder decision improved by this environment.

## 2) Construction Mode
- Hand-crafted expert world, programmatic/generated world, or hybrid.
- Why this mode is appropriate.
- Human/expert review boundary.
- Generator inputs, if generated.

## 3) World Model
- Entities and relationships.
- State variables, hidden state, mutable state, and reset semantics.
- Domain rules, policies, constraints, and invariants.
- Terminal success, terminal failure, timeout, and invalid-action states.

## 4) Tool/API Surface
- Tool names, schemas, permissions, side effects, and idempotence behavior.
- State read/write paths for every tool.
- Tool dependency graph: required orderings, optional orderings, and independent tools.
- Error behavior and tool-failure simulation.

## 5) Task Families
- Canonical families or subgraphs.
- Starting state distribution per family.
- Required evidence surfaces and final artifacts.
- Expected horizon, tool count, dependency count, and difficulty band.
- Negative criteria: privacy leak, unsupported claim, false completion, unauthorized mutation, escalation abuse, infrastructure probing, loop/retry pathology.
- Authorization-sensitive tasks must define required checks before mutation. Examples: identity verification, order/status verification, policy eligibility, amount limits, approval requirements, and auditable evidence.

## 6) Reward and Verification
- Verifier type: executable, expert rubric, LLM judge, hybrid, learned reward model.
- Per-criterion reward decomposition.
- Hidden/recomputed checks and alternate-valid-solution handling.
- Verifier provenance and calibration evidence.
- Integrity-clean success definition.
- Unsafe-but-passing action definition for support, finance, legal, medical, infrastructure, and security domains.

## 7) Splits and Leakage Boundary
- Train, dev, held-out eval, private held-out, and refresh stream boundaries.
- Public/private status and contamination risk.
- Canary strings or equivalent leakage probes.
- Agent-readable versus evaluator-only files, labels, tests, and metadata.

## 8) Testability Contract
- Minimal tasks exercising each state transition.
- Unit tests for tools and verifiers.
- Deterministic replay and reset checks.
- Reward-hacking probes and hardening checks.
- Task-quality admission thresholds.
