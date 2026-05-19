# Prompt Patterns

Use the smallest structure that removes ambiguity. For GPT-5.5-family prompts,
prefer outcome-first scaffolds and add process only when the exact path matters.

## Durable Ingredients

```text
Role:
Goal:
Success criteria:
Context and evidence:
Constraints and invariants:
Tools:
Validation:
Stop rules:
Output:
```

Do not force every section into every prompt. Include only the pieces that change behavior.
When migrating older prompts, remove process-heavy instructions that duplicate
the model's judgment unless they encode a real product, safety, tool, or
side-effect invariant.

## Execution Context Check

Before writing the prompt, answer:

- Is this prompt Codex-specific, another known harness, or portable?
- What context will the caller provide?
- What must the prompt state explicitly?
- What answer shape does the caller need back?

For portable prompts, avoid local file references, Codex-only tool names, approval mechanics, memory behavior, and project assumptions unless they are part of the target runtime.

## Prompt Surgery Checklist

- Preserve lines that already work.
- Identify the actual failure mode before rewriting.
- Remove ambiguity, contradictions, duplicate rules, and fake precision.
- Tighten tool rules and stopping criteria.
- Add output-shape instructions only if the consumer needs them.
- Prefer a few strong edits over a full rewrite.
- If the prompt keeps growing while the core issue remains, recommend a workflow or surface fix instead.

## Fresh Codex-Style Scaffold

```text
Role:
You are responsible for [job].

Goal:
[user-visible outcome]

Success criteria:
- [what must be true before the final answer]

Context:
[only context that changes behavior]

Constraints:
- Preserve:
- Avoid:
- Ask only if:

Tools:
- Use [tool] for [cases].
- Do not use [tool] for [cases].

Validation:
- Run [checks] when feasible.
- If blocked, report [specific blocker] and [next best check].

Stop rules:
- Stop when [core request can be answered or task is complete].
- Ask only when [missing information materially changes the outcome or risk].

Output:
- [desired answer or artifact shape]
```

## Prompt Repair Meta Prompt

```text
Here is the current prompt:
[PROMPT]

Desired behavior:
[DESIRED]

Observed failure:
[FAILURE]

While keeping as much of the existing prompt intact as possible:
1. Identify the smallest set of changes likely to fix the failure.
2. Explain why each change helps.
3. Return one revised prompt.
4. Return a second variant only if there is a real tradeoff.
5. If the failure is not primarily a prompt problem, say what should change instead.
```

## Step-Back Meta Prompt

```text
We have tried multiple prompt refinements and the result is still not meeting the goal.

Goal:
[GOAL]

Observed failures:
[FAILURES]

Current prompt or approach:
[PROMPT_OR_APPROACH]

Step back and rethink the problem.
1. Identify whether the real issue is prompt wording, missing context, invocation shape, tool/interface design, or evaluation criteria.
2. Explain why repeated prompt tweaks are or are not the right path.
3. Call out any brittle deterministic logic, such as heuristic hooks or prompt classifiers, that should be removed rather than refined.
4. Recommend the smallest broader change that would most likely fix the outcome.
5. Only provide a revised prompt if prompt wording is actually the main issue.
```
