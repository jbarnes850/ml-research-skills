# Skim-First Paper Writing

## Core principle
Most readers will skim. Optimize the paper so a reader who only sees the title,
abstract, section headers, figures, captions, and emphasized text can recover
the central claim, method or artifact, evidence, and scope boundary.

The skim layer is not marketing. It is a compressed evidence map. If a visible
claim is not supported by the body, weaken it; if decisive evidence is buried in
the body, surface it in the title, abstract, headers, captions, or figure plan.

## Skim layer
Produce or audit these surfaces:

- **Title:** shortest honest version of the contribution.
- **Abstract:** standalone summary of problem, gap, claim, evidence, and implication.
- **Introduction:** extended abstract that ends with claims, evidence preview, and contribution boundaries.
- **Section headers:** informative claims or section jobs, not generic labels.
- **Figures and tables:** takeaway-first visuals with self-contained captions.
- **Emphasis:** sparse bold or italics for claims, definitions, contrasts, and failure boundaries.

## Default output for skim-first tasks
Unless the user asks for a different format, use this order:

1. **Strongest skim failure:** the most important way the current surface misleads or loses a skimming reader.
2. **Skim path audit:** title, abstract, intro ending or contributions, section headers, figure/table captions, emphasized text.
3. **Claim ladder:** one-line claim, abstract claim, intro claim, header/caption claims, and body evidence.
4. **Evidence and overclaim boundary:** which visible claims are supported by experiments, figures, citations, or limitations; which claims must be weakened.
5. **Concrete rewrites:** title options, rewritten section headers, caption drafts, abstract/contribution edits as relevant.
6. **5-minute reader test:** what a skim-only reader can recover about the claim, method, evidence, limitation, and stakes.

This shape is a default, not a cage. For small requests, include only the
relevant parts, but do not omit the claim/evidence boundary when rewriting
visible paper-surface text.

For draft-from-notes or draft-from-paper tasks, still include the explicit
section names above. A polished skim layer without the audit, claim ladder, and
reader test is incomplete because the user cannot tell whether the surface is
clear or merely persuasive.

## Claim ladder
For broad drafting or review, build a ladder:

1. One-line paper claim.
2. Abstract-level claim.
3. Intro-level claim.
4. Section-header claims.
5. Figure/table caption claims.
6. Body evidence supporting each visible claim.

The ladder should preserve meaning while increasing detail. If a lower rung
does not support an upper rung, weaken the upper rung.

## Caption pattern
Use:

```
Context | Setup | Main result | Interpretation | Boundary if relevant
```

Captions should be understandable without reading the full surrounding section.
They should say what the reader is looking at, what comparison or condition is
being shown, what changed, and what conclusion is warranted.

When drafting captions, use the labels explicitly:

```
Caption draft:
- Context:
- Setup:
- Main result:
- Interpretation:
- Boundary:
```

This makes captions auditable. If a boundary is unknown, write "Boundary:
not established by the provided evidence" rather than omitting it.

## Header pattern
Prefer headers that let a reader reconstruct the argument.

Weak:

- Method
- Experiments
- Ablations

Stronger:

- Verifier-guided search converts extra samples into stronger N=1 outputs
- Hard-verifier selection beats likelihood ranking under fixed sample budgets
- Ablations show the verifier, not sampling alone, drives the gain

Do not force every header to be a claim. Background, notation, and setup
sections can use job-to-be-done headers when a claim would be artificial.

When rewriting headers, provide at least four concrete header rewrites unless
the paper section set is smaller. Label them as `Header rewrite:` so they are
easy to scan and review.

## Key figure plan
When a method or result can be visualized, propose one key figure that explains
the paper to a skimming reader. Specify:

- Figure type.
- Panels.
- Reader takeaway.
- Evidence shown.
- Caption draft.
- Claim supported.

If the method is hard to draw cleanly, say so and prefer a result or evidence
figure over a decorative method diagram.

## 5-minute reader test
Ask what a skimming reader can recover from only the title, abstract, section
headers, figures, captions, and emphasized text:

- What is the paper claiming?
- What is the method or artifact?
- What evidence supports it?
- What is the main limitation or scope boundary?
- Why should the reader care?

If the answer is incomplete, revise the skim layer before polishing prose.

## Review checklist
- Can the skim layer recover the claim, method, evidence, limitation, and stakes?
- Are section headers informative without overclaiming?
- Are figure/table captions self-contained?
- Is bold or italic emphasis sparse and attached to high-value claims or definitions?
- Does every visible claim map to experiment, figure, citation, or limitation?
