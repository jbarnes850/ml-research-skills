# Evidence and Experiments

## Evidence standards
- Evidence must be strong enough to update a skeptical reader.
- Quality beats quantity: prefer a few decisive experiments.
- Use multiple, diverse lines of evidence when possible.

## Red-teaming the narrative
- Assume a mistake exists. Where could it be?
- Identify alternative hypotheses and design experiments to distinguish them.
- Treat surprising results as higher risk; verify via independent checks.
- Simulate the skeptical reviewer: what would they attack first, and what
  missing experiment would most damage the paper?

## Experiment design
- Distinguish between hypotheses (results should differ if each is true).
- Check reliability: how surprised would you be if this is a bug?
- Check noise: would reruns look similar? Is variance reasonable?

## Ablations and baselines
- Ablate each major component to show necessity.
- Use strong baselines and tune them. Weak baselines undermine trust.
- Optimize boring baselines as hard as the new method.
- If related work contains a method applicable to the same problem setting,
  compare against it or explicitly explain why it is not applicable.

## Statistical rigor
- Avoid overclaiming on weak significance.
- If statistics matter, aim for stronger thresholds and report uncertainty.

## Pre/post-hoc clarity
- Mark which analyses were pre-specified vs after seeing results.
- Avoid cherry-picking; if examples are selected, say so explicitly.

## Example selection and cherry-picking
- If qualitative examples are used, say how they were chosen.
- Prefer random or representative examples unless you are making an existence-proof claim.
- If you present best cases, label them as such and show typical cases elsewhere.

## Reproducibility
- Provide enough detail to replicate.
- If possible, share code, configs, and key artifacts.
- Verify critical experiments via an alternate implementation path.
- Before writing: verify critical experiments (aim for most of them).
- If practical: run on a fresh machine; provide a quickstart notebook.

## Reviewer-risk pass
Before drafting strong claims, produce:

1. Top 3 reviewer attacks.
2. The missing baseline, ablation, seed, or statistical check most likely to
   sink acceptance.
3. The claim to weaken if that evidence remains unavailable.
4. The cheapest experiment or analysis that would reduce the largest risk.

## Review checklist
- Do results clearly discriminate among hypotheses?
- Are baselines strong and fair?
- Are ablations complete and interpretable?
- Is reproducibility adequate for a skeptical reader?
- Are all selected qualitative examples labeled as random, representative,
  typical, failure cases, or best cases?
