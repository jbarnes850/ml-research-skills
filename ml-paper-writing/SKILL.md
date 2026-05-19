---
name: ml-paper-writing
description: Draft, edit, and review ML research papers for evidence-backed claims, reviewer risk, and skim-first readability. Use for paper outlines, abstracts, introductions, section headers, figure/table captions, key figure plans, experiment/evidence plans, limitations, rebuttal-facing evidence, and claim-to-evidence audits. Do not use for purely mechanical bibliography formatting or generic prose editing unrelated to an ML research paper.
---

# ML Paper Writing

## Overview
Use this skill to turn research into a clear, evidence-backed narrative with 1-3 claims, strong experiments, and a reader-first structure.

## Task Routing

Choose the route that matches the user request:

- **Narrative / claims / abstract / intro:** load `references/narrative-claims.md`.
- **Evidence / experiments / reviewer risk / limitations:** load `references/evidence-experiments.md`.
- **Skim-first readability / section headers / captions / key figure / title:** load `references/skim-first-writing.md`.
- **Paper structure / section map / related work / polish:** load
  `references/structure-writing-process.md`.

For broad paper-planning requests, use the full workflow below. For narrow edits,
load only the relevant reference first and answer directly.

For skim-first, skimmability, title, section-header, caption, or key-figure
requests, default to the output shape in `references/skim-first-writing.md`
unless the user asks for a different format.

For skim-first paper-surface drafts, do not only produce polished title,
abstract, headers, or captions. Also include the skim path audit, claim ladder,
evidence/overclaim boundary, caption drafts, and 5-minute reader test so the
reader-facing surface stays tied to support.

## Full Workflow
1. **Define the narrative and claims**
   - Load `references/narrative-claims.md`.
   - Produce: 1-3 claims, motivation, novelty framing, and a 3-5 sentence narrative.

2. **Validate evidence and experiments**
   - Load `references/evidence-experiments.md`.
   - Produce: key experiments, ablations, baselines, reviewer objections, and red-team risks.

3. **Draft the structure and iterate**
   - Load `references/structure-writing-process.md`.
   - Produce: X-Y-Z-1 abstract outline, intro outline, section map, paragraph plan, and figure list.

## Default deliverables (choose what the user needs)
- Claims table: claim | confidence | key evidence | alternative hypotheses.
- Evidence map: claim | experiment/figure/citation | missing support | downgrade if missing.
- Abstract outline (5-7 sentences, cold-reader friendly).
- Intro outline (context, novelty, contributions).
- Skim path audit: title | abstract | intro ending | section headers | figure/table captions | emphasized text.
- Claim ladder: one-line claim | abstract claim | intro claim | section-header claims | caption claims | body evidence.
- 5-minute reader test: what a skimming reader can recover from title, abstract, headers, figures, captions, and emphasized text.
- Experiment plan with ablations and baselines.
- Figure plan with intended takeaways.
- Limitations and failure modes list.
- Reviewer-risk pass: top objections, missing experiment most likely to hurt acceptance, claim to weaken.

## Guardrails
- Inform, do not persuade. Avoid overclaiming.
- Define terms; assume the reader has less context than you do.
- Prefer a few decisive experiments over many weak ones.
- Be explicit about pre-registered vs post-hoc findings.
- Every externally visible claim must be supported by an experiment, figure,
  citation, or explicit limitation. If not, weaken or remove it.
- Treat the skim layer as a compressed evidence map, not marketing. If the
  title, abstract, headers, captions, or emphasized text overstate the evidence,
  weaken them.
- Prefer concrete reader-facing structure over generic writing advice.

## References
- `references/narrative-claims.md` for claims, novelty, and motivation.
- `references/evidence-experiments.md` for evidence standards, baselines, ablations.
- `references/skim-first-writing.md` for title, abstract, headers, captions, and skim-layer audits.
- `references/structure-writing-process.md` for abstract/intro structure and writing loop.
