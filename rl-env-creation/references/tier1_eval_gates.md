# Training and Evaluation Gates

These gates decide whether an environment is ready for training, evaluation, or a public claim.

## Pre-Training Hard Gates
- Capability and decision sentence is explicit.
- Environment contract covers state, tools, reward, splits, leakage boundary, and negative criteria.
- Tools compile/start and pass unit/property tests.
- Verifiers compile/start and pass known-positive, known-negative, and alternate-valid-answer tests.
- Deterministic replay works from reset state.
- Agent cannot write evaluator code, labels, hidden tests, metric scripts, or protected state.
- Task-quality report passes admission gates.
- Reward-hacking audit has no unresolved high-severity exploit path.
- Live model/tool backend is reachable; no silent mock fallback.
- Grouped rollout smoke has useful reward variance on key axes.

## Outcome Taxonomy
Do not collapse these into one pass/fail field:
- `Completed`: task intent satisfied and integrity-clean.
- `Partial`: meaningful progress, incomplete objective.
- `Agent Error`: invalid tool call, wrong reasoning, unsupported claim, false completion, unsafe action.
- `Environment Error`: tool/server/state bug blocked an otherwise valid attempt.
- `Verifier Error`: grader, judge, parser, or hidden check is wrong or unstable.
- `Leakage`: task success used answer-bearing metadata or private criteria.
- `Exploit`: success targeted evaluator mechanics rather than task intent.

## Metrics to Report
- Task success.
- Integrity-clean success.
- Exploit rate by category.
- Unsafe-action rate.
- Unsafe-but-passing action rate for authorization-sensitive domains.
- Environment/verifier error rate.
- Pass@k and repeated-run consistency.
- Success by capability axis, task family, difficulty band, horizon, tool count, and verifier type.
- Reward mean/std by group for group-normalized RL.
- Proxy reward versus gold/expert/executable signal when using LLM judges or learned rewards.

## Rollout Smoke
- Run a small live-policy sample before training.
- Inspect raw trajectories, not only aggregate metrics.
- Include easy, medium, hard, adversarial, and edge-case tasks.
- Include tool failures and reset/replay checks.
- Confirm the policy uses intended interfaces rather than direct file/db/config edits.

## Public Claim Gates
- Eval split is held out from training and checkpoint selection.
- Public/static benchmark contamination risk is stated and mitigated with private or refreshed tasks.
- All referenced assets, traces, validators, and reports exist.
- Claims cite source artifacts: contracts, logs, reports, verifier outputs, and raw trajectory samples.
