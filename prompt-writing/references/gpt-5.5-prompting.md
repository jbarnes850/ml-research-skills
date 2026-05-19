# GPT-5.5 Prompt Writing

## Core principle
GPT-5.5 works best when prompts define the outcome, success criteria, evidence,
constraints, and final answer shape, then leave room for the model to choose an
efficient path. Start from the smallest prompt that preserves the product
contract. Add process only when the exact path is a real requirement.

## Migration stance
When migrating an older prompt stack:

- Keep true invariants: safety, policy, side effects, output contracts, evidence requirements, and runtime-specific state rules.
- Remove process scaffolding that only compensates for older model weaknesses.
- Replace broad `ALWAYS` / `NEVER` instructions with decision rules unless the rule is truly absolute.
- Prefer API features over prompt text when available, especially Structured Outputs, `text.verbosity`, `reasoning.effort`, prompt caching, and tool descriptions.
- Re-evaluate `low` and `medium` reasoning effort before escalating to `high` or `xhigh`; higher effort should earn its cost in evals.

## Default output for GPT-5.5 prompt work
Unless the user asks for a different shape, return:

1. **Diagnosis:** the prompt/runtime failure or improvement target.
2. **Runtime Contract:** runtime, caller-provided context, side effects, evidence needs, and output consumer.
3. **Revised Prompt:** an outcome-first prompt with only necessary process.
4. **Model and Runtime Settings:** recommended `reasoning.effort`, `text.verbosity`, structured output or schema handling, caching, and tool/preamble/phase guidance where relevant.
5. **Validation Plan:** representative evals or checks that would prove the prompt improved.
6. **Why This Is Better:** bullets tied to behavior, not taste.

For simple edits, compress this into diagnosis, revised prompt, and validation.

Use these exact section labels for substantial GPT-5.5 prompt tasks:

```text
## Diagnosis
## Runtime Contract
## Revised Prompt
## Model and Runtime Settings
## Validation Plan
## Why This Is Better
```

Do not replace these sections with looser labels such as "Critique",
"Retrieval Budget", "Runtime Notes", "Brief Explanation", or "Recommended
Settings" unless the user explicitly asked for a different report format. Those
labels can be subsections, but the six sections above should remain present so
the artifact is easy to evaluate.

When the user asks for a brief explanation, keep the six sections but make each
one short. Do not omit **Model and Runtime Settings** or **Validation Plan**;
these are often the difference between a prompt that looks good and a prompt
that can be deployed.

If the task is a migration, explicitly name what changed from the old model
assumptions: process removed, invariants preserved, output contract retained,
and reasoning/verbosity defaults to test.

Name concrete removed rules from the source prompt. For example, if the old
prompt required "always search three times", "always use high reasoning", or
"explain the full process", say those were removed or converted into a
retrieval budget, runtime setting, or conditional decision rule.

For a substantial prompt rewrite, the **Revised Prompt** itself should usually
expose the contract with these headings, unless a stricter user-provided format
prevents it:

```text
Role:

# Goal

# Success criteria

# Constraints

# Runtime and tools

# Output

# Stop rules
```

This is not decorative formatting. It makes the runtime contract skimmable,
testable, and easier to compare against eval failures. Include all six ideas
even if some sections are only one or two bullets.

Do not rename these headings to domain-specific alternatives. For example,
"Evidence rules" belongs under `# Constraints`, "Retrieval budget" belongs
under `# Runtime and tools`, and "Final check" belongs under `# Stop rules`.

## Outcome-first prompt shape
Use this as a starting point for complex prompts:

```text
Role:
[1-2 sentences defining the model's function and caller contract]

# Personality
[tone and collaboration style, only if it changes UX]

# Goal
[user-visible outcome]

# Success criteria
[what must be true before final answer]

# Constraints
[policy, safety, evidence, side-effect, and business limits]

# Runtime and tools
[tool, retrieval, state, preamble, phase, and side-effect rules when relevant]

# Output
[sections, length, tone, and stable fields if needed]

# Stop rules
[when to retry, search, ask, fallback, abstain, or stop]
```

Avoid replacing this shape with a long chronological checklist. If process is
needed, place it under `# Runtime and tools` or `# Stop rules`, and keep it
subordinate to the outcome.

## Personality and collaboration style
Use personality to shape experience, not to compensate for unclear goals.

- Personality controls tone, warmth, directness, formality, humor, empathy, and polish.
- Collaboration style controls when the assistant asks questions, makes assumptions, uses tools, gives context, checks work, and handles uncertainty.
- Keep both short. They should not replace goals, success criteria, tool rules, or stopping conditions.

## Retrieval budgets
For grounded answers, define when retrieval is enough:

- Start with the minimum search or document read likely to answer the core request.
- Search again only when the core question is unanswered, a required fact/date/ID/source is missing, the user asked for exhaustive coverage, or an important claim would otherwise be unsupported.
- Do not search again for phrasing, nonessential examples, or claims that can safely be made generic.
- Absence of evidence is not automatically evidence of absence; say what was checked and what remains unknown.

## Tool-heavy Responses workflows
For multi-step or tool-heavy tasks:

- Add a short preamble rule when visible responsiveness matters: before tools, send a 1-2 sentence update with the first step.
- If the application manually replays assistant items, preserve `phase` exactly; use commentary/intermediate phases for updates and final-answer phases for completion.
- Include enough-evidence stop rules: after each retrieval/tool result, stop when the core request can be answered with required support; continue only when a required fact, date, ID, source, action precondition, or validation result is missing.
- Include bounded retry rules: retry transient failures with changed parameters at most 2 times; do not retry deterministic failures with identical inputs.
- Put tool-specific behavior in tool descriptions when possible: purpose, when to use, required inputs, side effects, retry safety, and common errors.
- Add workflow-level tool rules only when they apply across tools or materially change policy.

## Validation and stopping
Prompt the model to check work when checks are available:

- Coding: targeted tests, type checks, lint, build, or smoke tests.
- Visual artifacts: render and inspect for layout, clipping, missing content, and consistency.
- Grounded answers: cite precise support for factual claims and stop when enough evidence exists.
- Plans: map requirements to files, APIs, data flow, failure behavior, and validation.

Do not optimize for few tool calls over correctness, evidence, or required validation.

For prompt migrations and repairs, always include a **Validation Plan** unless
the user asks for prompt-only output. The plan should contain representative
pass/fail eval checks, not just general advice. Good checks name:

- the input scenario,
- the expected behavior,
- the failure that would prove the prompt regressed,
- any runtime setting or tool contract that must be tested.

## Model and runtime settings
For GPT-5.5 prompt artifacts, usually include a short settings note:

Use explicit lines so the caller can test the runtime rather than infer it:

```text
- reasoning.effort: medium by default; test low for latency-sensitive paths before escalating, and use high/xhigh only after eval gains justify the cost.
- text.verbosity: low for concise production answers, medium for synthesis or review artifacts.
- Structured Outputs/schema: use Structured Outputs when the caller needs stable machine-readable fields; otherwise keep the prose output contract short.
- Prompt caching: place stable role, policy, tool, and output contract text before dynamic context.
- Tool descriptions: put tool-specific purpose, inputs, side effects, retry safety, and common errors in the tool schema/description when possible.
- Preamble/phase: for tool-heavy Responses workflows, allow short commentary preambles and preserve assistant-item phase values during replay.
```

For prompt repairs, state which settings should be evaluated first rather than
declaring a permanent value.

## Invariants vs decision rules
Separate absolute requirements from judgment calls:

- **True invariants:** safety/policy limits, output fields, side effects, citation requirements, state replay requirements, privacy/security limits, and actions that must never occur.
- **Decision rules:** when to search, ask, retry, use a tool, escalate effort, add examples, or stop. Phrase these as conditions, not broad `ALWAYS` / `NEVER` rules.
- **Prompt bloat check:** remove instructions that only repeat the goal, restate common sense, prescribe unnecessary order, or compensate for missing tool/runtime design.

When explaining the rewrite, explicitly mention preserved invariants and
absolute rules converted into decision rules when applicable.

In **Why This Is Better**, prefer these labels when relevant:

```text
- True invariants preserved: ...
- Judgment-call decision rules: ...
- Prompt bloat removed: ...
- Runtime contract clarified: ...
```

## Anti-patterns
- Carrying over every line from an older prompt stack without testing whether it still helps.
- Process-heavy step lists when only the outcome matters.
- Repeating output schemas in prompt text when Structured Outputs can enforce them.
- Adding absolute rules for judgment calls.
- Hiding retrieval, citation, or validation requirements inside vague style guidance.
- Using high reasoning effort to compensate for ambiguous goals, weak stop rules, or open-ended tools.
