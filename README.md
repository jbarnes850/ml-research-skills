# ML Research Skills

Five shareable Codex / agent skills for ML research work:

- `ml-paper-writing`: draft, edit, and review ML research papers around evidence-backed claims, reviewer risk, and skim-first readability.
- `ml-research-design`: design ML experiments, hypotheses, ablations, evaluation plans, go/no-go criteria, and research prioritization from first principles.
- `prompt-writing`: write, repair, critique, or migrate prompts for tool-using agents, GPT-5.5-family workflows, Responses API prompts, and failed runtime prompts.
- `rl-env-creation`: build or audit verifier-backed RL environments with task-quality gates, reward-hacking checks, and training-readiness criteria.
- `ml-experiment-controls`: use control conditions as bug detectors in ML experiments and separate format, compression, and intervention hypotheses.

## Install

Install a specific skill with the Skills CLI:

```bash
npx skills add jbarnes850/ml-research-skills --skill ml-paper-writing -g -y
npx skills add jbarnes850/ml-research-skills --skill ml-research-design -g -y
npx skills add jbarnes850/ml-research-skills --skill prompt-writing -g -y
npx skills add jbarnes850/ml-research-skills --skill rl-env-creation -g -y
npx skills add jbarnes850/ml-research-skills --skill ml-experiment-controls -g -y
```

Install all skills at once:

```bash
npx skills add jbarnes850/ml-research-skills --all -g
```

Or clone the repository and copy a skill folder into your local skills directory:

```bash
git clone https://github.com/jbarnes850/ml-research-skills.git
cp -R ml-research-skills/ml-paper-writing ~/.codex/skills/
cp -R ml-research-skills/ml-research-design ~/.codex/skills/
cp -R ml-research-skills/prompt-writing ~/.codex/skills/
cp -R ml-research-skills/rl-env-creation ~/.codex/skills/
cp -R ml-research-skills/ml-experiment-controls ~/.codex/skills/
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

### `prompt-writing`

Use this when prompt wording is the artifact, or when a prompt has failed in a specific runtime and needs diagnosis, a runtime contract, a revised prompt, model/runtime settings, and a validation plan.

Included files:

```text
prompt-writing/
├── SKILL.md
└── references/
    ├── gpt-5.5-prompting.md
    └── prompt-patterns.md
```

Typical invocation:

```text
Use $prompt-writing to repair this agent prompt after the observed tool-routing failure.
```

### `rl-env-creation`

Use this when creating, scaling, or auditing RL environments for LLM/agent training, especially verifier-backed task corpora, tool sandboxes, seed generators, reward-hacking audits, and training readiness gates.

Included files:

```text
rl-env-creation/
├── SKILL.md
├── references/
│   ├── environment_scaling_patterns.md
│   ├── graph_contract_template.md
│   ├── literature_review.md
│   ├── reward_hacking_audit.md
│   ├── task_distribution_targets.md
│   ├── task_quality_gates.md
│   ├── telemetry_single_run.md
│   └── tier1_eval_gates.md
└── scripts/
    ├── seed_mix_audit.py
    └── task_quality_audit.py
```

Typical invocation:

```text
Use $rl-env-creation to audit this generated task corpus before any RL run.
```

### `ml-experiment-controls`

Use this when designing ablations, debugging unexpected baseline results, or deciding whether a control condition failure indicates a bug instead of a real experimental effect.

Included files:

```text
ml-experiment-controls/
└── SKILL.md
```

Typical invocation:

```text
Use $ml-experiment-controls to diagnose why this additive control underperformed the reference baseline.
```

## Repository Layout

Each top-level folder is a complete skill package. `SKILL.md` contains the trigger metadata and core workflow; `references/` contains progressively loaded supporting material. The folders are intentionally kept installable as independent skills.
