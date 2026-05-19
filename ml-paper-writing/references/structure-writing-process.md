# Structure and Writing Process

## Writing loop (iterative)
1. Abstract draft (1-2 paragraphs).
2. Bullet narrative (claims + evidence + impact).
3. Intro outline (motivation, context, claims, evidence).
4. Paragraph outline: one line per paragraph, one idea per line.
5. Full outline (methods, results, limitations).
6. First draft, keeping the paragraph summary as a comment or note above each paragraph while drafting.
7. Reflect, revise, delete fluff, repeat.

Spend comparable effort on: title, abstract, intro, figures, and the rest.
Plan for feedback after each step; outlines are fastest to review.

## Paper structure (default)
- Abstract: cold-start reader, claims, key evidence, impact.
- Introduction: extended abstract with context, novelty, and contributions.
- Related work: academic siblings; compare and contrast assumptions, methods,
  and applicability rather than merely summarizing papers.
- Background: academic ancestors; concepts, notation, and prior work required
  to understand the method.
- Problem setting: use as a separate section when the setting itself is novel.
- Main body: methods, experiments, results, interpretation.
- Method: what we do and why, using the formalism already introduced.
- Experimental setup: specific instantiation, implementation details, metrics,
  hyperparameters, and fairness/comparability details.
- Results and discussion: baselines, statistics or confidence intervals,
  ablations, interpretation, and limitations.
- Figures: communicate key evidence; captions should stand alone.
- Discussion/limitations: calibrated limitations and implications.
- Appendix: full technical detail, extra experiments.

## Abstract pattern
- Sentence 1: broad context.
- Sentence 2: gap/problem.
- Sentence 3: main claim.
- Sentence 4: evidence or method cue.
- Final: impact and why it matters.

## Introduction pattern
- Context and motivation.
- Technical background (with citations).
- Main claims and evidence preview.
- Contributions list (bullet points).

## Figures and tables
- Decide the takeaway first, then choose a visualization.
- Highlight key curves and annotate critical results.
- Captions should include context, interpretation, and key details.

## Style guidance
- Inform, do not persuade.
- Precision over jargon; define terms.
- Avoid verbosity and overclaiming.
- Fight the illusion of transparency: restate key ideas in multiple forms.
- Be clear about contribution boundaries: never blur prior work and this paper.
- Avoid filler words, grandiose adjectives, anthropomorphism, and unsupported
  subjective claims.
- Avoid synonyms for work-specific terminology; use one term consistently.
- Introduce acronyms and symbols before use, and only introduce ones reused in
  the paper.
- Cite any claim not supported by the paper's experiments.
- Check broken references, citations, figure/table numbers, and acronym use in
  the rendered PDF.
- After the first draft, try deleting roughly one third of the words while
  preserving the claims and evidence.

## Paragraph outline pattern
For section drafts, prefer:

```
Paragraph 1: [one-line takeaway]
Paragraph 2: [one-line takeaway]
Paragraph 3: [one-line takeaway]
```

Then expand each line into prose. If a paragraph cannot be summarized in one
line, split it or clarify the point.

## Review checklist
- Can a cold reader restate the claims?
- Are key results highlighted in figures?
- Are limitations explicit and honest?
- Does related work compare and contrast rather than summarize?
- Does every section have a job in proving the paper's central claims?
