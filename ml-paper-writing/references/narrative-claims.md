# Narrative and Claims

## Core idea
A strong ML paper is a short, rigorous, evidence-based narrative. The paper exists to support 1-3 concrete claims that fit a single theme. Everything else is supporting evidence, clarity, and context.

## Claim selection
- Pick 1-3 claims that are concrete and testable.
- Prefer a cohesive theme, not a grab-bag.
- Decide the confidence level:
  - Existence proof (one clear example).
  - Systematic (common across contexts).
  - Narrow (best under conditions X, Y).
  - Hedged (suggestive evidence).
- Avoid overclaiming; stronger claims require stronger evidence.

## Evidence-to-claim traceability
For each externally visible claim, identify its support:

- **Experiment or figure:** direct evidence from this paper.
- **Citation:** prior work supports the background claim.
- **Limitation:** the paper does not prove this; state the boundary.
- **Downgrade:** weaken the claim if support is incomplete.

If no support exists, remove the claim. Do not let a narrative outrun the
evidence just because it makes the paper feel cleaner.

## Motivation and impact
- Answer: What problem is being solved? Why should readers care?
- Tie claims to the bigger picture (practical impact, scientific insight, or correcting a misconception).

## Illusion of transparency (explicitly address)
- Assume readers lack your context and will misinterpret unless you guide them.
- Repeat key ideas in varied ways (abstract, intro, figures, captions).
- Define terms and techniques; do not assume shared tacit knowledge.

## Novelty framing
- Be explicit about what is novel vs what is established.
- Novelty can be a rigorous replication, a correction, or a better method.
- Explain why prior work was insufficient and how your results update beliefs.

## When to start writing
- List what you have learned; choose the most compelling items.
- Ask whether you can defend each claim with rigorous evidence.
- Prefer writing once at least one claim has strong support.

## Narrative compression exercise
1. Write a 3-5 sentence narrative: problem, claim, evidence, impact.
2. Ask what is missing, what is extraneous, what is misleading.
3. Iterate until the narrative is clean and defensible.

## Abstract / intro X-Y-Z-1 pattern
Use this as the default ML-paper skeleton:

- **X:** What are we trying to do, and why is it relevant?
- **Y:** Why is this hard or unresolved?
- **Z:** What is our contribution?
- **1:** How do we verify that we solved it?
  - **1a:** Experiments and results.
  - **1b:** Theory or mechanism, if applicable.

The introduction is the longer version of the abstract. It should preserve the
same logic while adding context, novelty, contribution boundaries, and an
evidence preview.

## Narrative prompting questions
- Which result would be most exciting to show a peer?
- What would make someone care about this problem?
- What was hard or novel that others have not done?
- What would a skeptical reader doubt first?
- Which claim should be weakened if the next experiment fails?

## Review checklist
- Are the claims concrete and falsifiable?
- Is the motivation clear to a cold reader?
- Is the novelty explicit and modest?
- Would a skeptical reader update their beliefs?
- Did you explicitly counter the illusion of transparency?
