---
name: rl-env-creation
description: Build or audit RL environments for LLM/agent training with task-centric world models, scalable environment synthesis, executable/rubric rewards, reward-hacking probes, task-quality QA, and pre-training readiness gates. Use when creating, scaling, or evaluating agentic RL environments, seed generators, MCP/tool sandboxes, workplace simulations, coding/data environments, or verifier-backed task corpora.
---

# RL Environment Creation

## Default Stance
An RL environment is not good because it has many tools, entities, or generated tasks. It is good only if it produces diverse, difficult, realistic, verifiable tasks whose rewards measure the intended capability without leaking shortcuts.

The working order is: rubric before schema, schema before environment, environment before training. Training is allowed only after the task-quality and reward-hacking gates pass.

## Workflow

### 1) State the capability and decision
- Name the capability axis: tool use, planning, adaptability, groundedness, domain reasoning, recovery, safety, or another explicit axis.
- Name the stakeholder decision the environment will improve.
- Write the training justification sentence before any RL run: "This training run is worth doing because it will improve [decision] for [stakeholder] as measured by [rubric/eval], producing [artifact/behavior]."
- If the sentence is weak, stop at environment/rubric work.

### 2) Choose the environment construction mode
- Hand-crafted expert world: prefer when realism, business rules, edge cases, and rubrics matter more than scale.
- Programmatic/generated world: prefer when many tool-interaction sandboxes can be synthesized and verified automatically.
- Hybrid: use generated breadth, then expert review/admission for high-value task families.
- Record the choice and tradeoff in an environment contract. Use `references/graph_contract_template.md`.

### 3) Build a task-centric world contract
- Define entities, state, transitions, tool/API actions, hidden state, terminal states, and reset semantics.
- Every task family must map to state transitions and observable evidence.
- Tools must be executable against real state, not text-only simulacra, unless the explicit research question is simulator fidelity.
- Use `references/environment_scaling_patterns.md` for hand-crafted, generated, and hybrid patterns.

### 4) Design rewards before scaling tasks
- Prefer executable verifiers when correctness can be recomputed.
- Use expert-authored rubrics/checklists when tasks are open-ended, but make each criterion independently inspectable.
- Avoid single scalar holistic rewards as the only signal. Decompose reward into correctness, constraint satisfaction, process/evidence use, format, safety/integrity, and efficiency where relevant.
- Require hidden or recomputed checks for any task that can be gamed by visible schemas, metadata, or public tests.

### 5) Admit tasks through QA, not vibes
- Measure distribution by environment, task family, capability axis, difficulty band, tool count, horizon/turn count, verifier type, and source/provenance.
- Require solvability evidence: reference solution, executable solution, expert solution, or model-panel attempts with consistent pass/fail behavior.
- Keep a held-out evaluation split whose tasks, seeds, hidden tests, and verifier internals are not used for training or checkpoint selection.
- Use `references/task_quality_gates.md`, `references/task_distribution_targets.md`, and, when metadata exists, `scripts/task_quality_audit.py`.

### 6) Run a reward-hacking audit
- Threat-model leakage, tampering, sequence manipulation, proxy/parser exploits, visible-test overfitting, denial-of-evaluation, evaluator bias, and reward-model drift.
- Harden the environment before training: strict schemas, fail-closed parsing, protected evaluator paths, reduced file access, randomized intermediates, recomputed dependencies, and hidden/adversarial variants.
- Track exploit rate separately from task success. A task that succeeds by exploiting the harness is a failed environment datum.
- In authorization-sensitive domains, track unsafe-but-passing actions as failures even when the surface task reward is positive.
- Use `references/reward_hacking_audit.md`.

### 7) Gate training readiness
- Run compile/lint/unit checks for tools and verifiers.
- Run deterministic replay and reset/idempotence checks.
- Preflight live model/tool backends; no silent mock fallback.
- Compute reward variance for group-normalized RL. Stop if key axes have mostly near-zero within-group variance.
- Run small smoke rollouts and inspect raw trajectories before any large run.

### 8) Produce artifacts
For every serious environment pass, produce:
- `environment_contract`: world model, state transitions, tools, reset semantics, construction mode.
- `task_quality_report`: task distribution, difficulty calibration, solvability, split boundaries, provenance.
- `reward_hacking_report`: exploit taxonomy coverage, hardening decisions, exploit rate, residual risks.
- `training_readiness`: validation commands, smoke results, reward variance, go/no-go.

## Stop Conditions
- No explicit capability axis or stakeholder decision.
- Reward is a proxy with no anti-hacking audit.
- Task distribution is dominated by one family, one difficulty band, one source, or one visible verifier pattern.
- Solvability is unknown, trivial, or only demonstrated by the generator that wrote the task.
- Eval split leaks generator seeds, hidden tests, verifier internals, or task-adjacent metadata.
- Live rollout uses mocks, fallback policies, or uninspected trajectories.

## Resources
- `references/literature_review.md`: source map and lessons from 2025-2026 environment and reward-hacking work.
- `references/environment_scaling_patterns.md`: construction patterns for expert, generated, and hybrid environments.
- `references/graph_contract_template.md`: environment/world contract template.
- `references/task_quality_gates.md`: admission and difficulty QA gates.
- `references/task_distribution_targets.md`: default distribution targets and red flags.
- `references/reward_hacking_audit.md`: exploit taxonomy and hardening checklist.
- `references/tier1_eval_gates.md`: rollout/training readiness gates.
- `references/telemetry_single_run.md`: single-run telemetry hygiene.
- `scripts/task_quality_audit.py`: metadata distribution and gate audit for JSON/JSONL task manifests.
- `scripts/seed_mix_audit.py`: legacy prompt-injection seed mix audit for old opensec-style manifests.
