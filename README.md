# ML Research Skills

Two shareable Codex / agent skills for ML research work:

- `ml-paper-writing`: draft, edit, and review ML research papers around evidence-backed claims, reviewer risk, and skim-first readability.
- `ml-research-design`: design ML experiments, hypotheses, ablations, evaluation plans, go/no-go criteria, and research prioritization from first principles.

## Install

Install either skill with the Skills CLI:

```bash
npx skills add jbarnes850/ml-research-skills --skill ml-paper-writing -g -y
npx skills add jbarnes850/ml-research-skills --skill ml-research-design -g -y
```

Install both at once:

```bash
npx skills add jbarnes850/ml-research-skills --all -g
```

Or clone the repository and copy a skill folder into your local skills directory:

```bash
git clone https://github.com/jbarnes850/ml-research-skills.git
cp -R ml-research-skills/ml-paper-writing ~/.codex/skills/
cp -R ml-research-skills/ml-research-design ~/.codex/skills/
```

## Skills

### `ml-paper-writing`

Use this when working on ML paper narratives, abstracts, introductions, section headers, captions, key figures, experiment plans, limitations, rebuttals, or claim-to-evidence audits.

Included files:

```text
ml-paper-writing/
├── SKILL.md
└── references/
    ├── evidence-experiments.md
    ├── narrative-claims.md
    ├── skim-first-writing.md
    └── structure-writing-process.md
```

Typical invocation:

```text
Use $ml-paper-writing to audit this paper draft for overclaims and reviewer risk.
```

### `ml-research-design`

Use this when designing experiments, forming falsifiable hypotheses, prioritizing research directions, critiquing methodology, planning RL/LLM evaluation, or defining go/no-go criteria.

Included files:

```text
ml-research-design/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── hypothesis-framework.md
    ├── problem-selection.md
    └── sources.md
```

Typical invocation:

```text
Use $ml-research-design to critique this experiment plan and define the cheapest belief-updating test.
```

## Repository Layout

Each top-level folder is a complete skill package. `SKILL.md` contains the trigger metadata and core workflow; `references/` contains progressively loaded supporting material. The folders are intentionally kept installable as independent skills.
