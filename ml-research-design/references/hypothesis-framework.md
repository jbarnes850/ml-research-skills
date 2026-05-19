# Hypothesis Formation and Testing Framework

Structured protocol for forming strong hypotheses and designing experiments
that produce decisive evidence. Grounded in Sakana AI (2026), Karpathy's
systematic methodology, and Schulman's goal-driven research framework.

## Phase 1: Problem Decomposition

Before forming a hypothesis, decompose the research question into its
constituent uncertainties.

### The Uncertainty Map

For any research question, enumerate:

1. **Mechanistic uncertainties:** What causal mechanisms are unknown?
   Example: "Does GRPO's group normalization suppress learning signal when
   reward variance is low within groups?"

2. **Empirical uncertainties:** What quantities are unknown?
   Example: "What fraction of reward axes produce zero-variance groups
   at initialization?"

3. **Methodological uncertainties:** What design choices lack justification?
   Example: "Is group size 8 optimal, or was it inherited from the reference
   implementation without validation?"

4. **Boundary uncertainties:** Where does the approach break?
   Example: "At what curriculum difficulty level does the RL signal degenerate
   to noise?"

Rank uncertainties by: (a) how much resolving them would change the research
direction, and (b) how cheaply they can be tested.

## Phase 2: Hypothesis Construction

A strong hypothesis has five properties:

### 1. Falsifiability
State the hypothesis such that a specific observation would *disprove* it.

- Weak: "RLVR improves reasoning."
- Strong: "RLVR with GRPO on math tasks increases solve rate by >5% over
  SFT baseline at equal compute, measured on MATH-500."

### 2. Mechanism
Name the causal pathway.

- Weak: "Curriculum learning helps."
- Strong: "Monotonically increasing task difficulty produces a curriculum
  that maintains reward signal in the learnable zone (advantage variance
  >1e-3), preventing both trivial convergence and gradient starvation."

### 3. Surprise Value
A hypothesis worth testing should have a non-obvious prediction. If both
outcomes (confirmed/disconfirmed) would be unsurprising, the experiment
does not produce new knowledge.

Ask: "What would a skeptical reviewer find interesting about either outcome?"

### 4. Scope
Explicitly bound what the hypothesis covers and does not cover.

- "This hypothesis applies to single-turn math reasoning tasks with
  verifiable answers. Extension to open-ended generation is a separate claim."

### 5. Alternatives
For every hypothesis H1, articulate at least one competing hypothesis H2
that predicts a different observation under the same experiment.

- H1: "Performance improvement comes from the RL optimization signal."
- H2: "Performance improvement comes from the additional training data
  exposure during rollouts, independent of reward."
- Discriminating experiment: Compare RL training vs. continued SFT on the
  same rollout data without reward signal.

## Phase 3: Minimum Viable Experiment (MVE)

The MVE is the cheapest experiment that produces decisive evidence for or
against the hypothesis.

### Reality-Contact Menu

Before proposing a full run, ask which cheap contact with reality can collapse
the uncertainty fastest:

- **Toy example:** the minimal synthetic setting where the core mechanism must
  appear if the idea is real.
- **Simplified baseline:** the boring method that should fail if the new method
  is needed.
- **Mocked component:** replace expensive or unreliable components with a
  cheating implementation when they are not the key uncertainty.
- **Formal counterexample:** a small construction that would make the claim
  false before any GPU spend.
- **Ablated pipeline smoke:** end-to-end run on tiny data that verifies logging,
  metrics, gradients, and evaluation plumbing.

Use the cheapest option that can invalidate the direction. Full-scale runs are
for resolving scale-sensitive uncertainties, not for discovering that the basic
mechanism was never present.

### Design Principles

1. **Attack the riskiest assumption first.** The riskiest assumption is the
   one most likely to invalidate the entire research direction. Test it before
   investing in infrastructure.

2. **One variable at a time.** Change exactly one thing from baseline. If you
   must change multiple things, establish that each change in isolation has
   the expected effect before combining.

3. **Dumb baselines first.** Before any sophisticated model, establish:
   - Random baseline (lower bound)
   - Strongest known existing method (upper bound)
   - Linear model or majority-class predictor (sanity check)

4. **Fixed random seeds.** Reproducibility is non-negotiable. Report mean
   and standard deviation across 3+ seeds minimum.

5. **Karpathy's staged ladder:**
   - Stage 1: Verify end-to-end pipeline on trivial data
   - Stage 2: Overfit a single batch (confirms model capacity)
   - Stage 3: Train on full data with no regularization (confirms signal)
   - Stage 4: Add regularization (improves generalization)
   - Stage 5: Tune hyperparameters (marginal gains)
   Never skip stages. Failures at stage N invalidate all later stages.

### Cost Estimation

Before launching any experiment, estimate:
- Wall-clock time per step
- Total steps
- Total compute cost
- Checkpoint schedule
- What result at each checkpoint would cause early stopping

### RLVR-Specific: Reward Variance Gate

Before ANY RL training with group normalization (GRPO, GDPO):

```python
group_std = rewards[axis].reshape(-1, group_size).std(dim=-1)
zero_frac = (group_std < 1e-5).float().mean()
```

If ANY axis has >50% zero-std groups: STOP. Zero gradient. Binary axes,
deterministic-per-seed penalties, and fixed-environment rewards are
structural risks. This check takes <1 min on CPU and prevents $50-200
in wasted compute.

## Phase 4: Result Interpretation

### The Decision Reasoning Pattern

Before every experiment, write the prediction. After every experiment, complete
the update:

```
Hypothesis: [H1]
Experiment: [What I did]
Expected: [What I predicted]
Observed: [What actually happened]
Surprise: [What I did not expect, if anything]
Interpretation: [What this means for H1 and alternatives]
Source of error: [execution bug, noise, confound, or bad research judgment]
Next: [Updated hypothesis or next experiment]
```

If a mentor, reviewer, or collaborator would predict a different outcome, state
that prediction too. Differences between your prediction and theirs are useful
training data for research taste.

### Handling Ambiguous Results

When results neither clearly confirm nor disconfirm:

1. Check for bugs first (visualization, gradient flow, data pipeline)
2. Compute effect size and confidence intervals, not just p-values
3. Ask: "Is the effect size large enough to matter for the research goal?"
4. Ask: "Is the experiment sufficiently powered to detect the expected effect?"
5. If underpowered, increase scale. If powered and null, update beliefs.

### Negative Results

Negative results are information. Document:
- What was ruled out
- What constraints this places on future directions
- Whether the negative result generalizes or is specific to the setup

A well-documented negative result that rules out a plausible direction is
more valuable than a weakly positive result that doesn't update beliefs.

## Phase 5: Iteration

### When to Pivot

Pivot when:
- Three consecutive experiments produce null results on the core hypothesis
- The estimated compute to achieve a meaningful result exceeds budget by 3x
- A competing group publishes a strictly better approach to the same problem
- The problem itself becomes less important (field shifts)

Do not pivot when:
- A single experiment fails (debug first)
- Results are noisy but trending in the right direction
- The approach is working but slower than hoped

### When to Deepen

Deepen (rather than broaden) when:
- Initial results show a clear signal but with unexplained variance
- The mechanism is unclear despite positive results
- Ablations reveal unexpected sensitivities

### Schulman's Exploration Budget

Allocate 10-20% of research time to exploratory work outside the main line.
This prevents tunnel vision and seeds future directions. Track exploration
separately from main-line progress.
