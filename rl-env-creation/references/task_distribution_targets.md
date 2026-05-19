# Task Distribution Targets

These are defaults. Replace with domain-specific targets once the world contract and capability axes are known.

## Capability Axis Coverage
- Tool use: 15-25%
- Planning/workflow ordering: 15-25%
- Groundedness/evidence use: 15-25%
- Domain rules/common sense: 15-25%
- Adaptability/recovery: 10-20%
- Safety/authorization/privacy: 5-15%

## Difficulty Bands
- Easy sanity tasks: 10-20%
- Medium operational tasks: 35-50%
- Hard multi-step tasks: 25-40%
- Adversarial/edge-case tasks: 10-20%

## Verifier Mix
- Executable/recomputed: target as high as the domain allows.
- Expert rubric: required for open-ended human-facing tasks.
- LLM judge: use only with rubric decomposition and calibration.
- Learned reward model: use only with held-out gold checks and overoptimization monitors.

## Split Discipline
- Train: admitted tasks only.
- Dev: generator/verifier iteration only; not for checkpoint claims.
- Eval: held out from training and generation tuning.
- Private eval or refresh: needed for public/static benchmarks or contamination-sensitive claims.

## Red Flags
- One task family exceeds 50% without an explicit scope decision.
- One difficulty band exceeds 60%.
- One verifier template dominates and has not been stress-tested.
- More than 10% of tasks lack solvability evidence.
- Any eval task exposes answer-bearing metadata or evaluator internals.
