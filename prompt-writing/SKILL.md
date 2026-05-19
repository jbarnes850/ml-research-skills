---
name: prompt-writing
description: Use when writing, repairing, critiquing, or migrating system prompts, developer prompts, reusable task prompts, GPT-5.5 prompts, tool-using prompts, Responses API prompts, automation prompts, or prompts that have failed in a specific runtime.
---

# Prompt Writing

## Overview

Use this skill when the wording is the artifact, or when repeated wording changes may be hiding a deeper runtime, context, tool, or evaluation problem.

## Core Rules

1. Match the runtime and caller contract first.
   - Identify where the prompt will run.
   - Identify what context the caller will actually provide.
   - Identify the expected output shape.
   - Do not rely on ambient chat context unless that context will exist at runtime.

2. Preserve what already works.
   - For prompt repair, identify the observed failure before editing.
   - Keep lines that are already carrying behavioral weight.
   - Prefer the smallest strong edit over a full rewrite.
   - Provide a second variant only when there is a real tradeoff.

3. Prefer surface fixes over prompt bloat.
   - If the prompt keeps growing without fixing the behavior, step back.
   - Diagnose whether the real issue is missing context, surface choice, invocation shape, tool design, or evaluation criteria.
   - Move repeated stable behavior to `AGENTS.md`, a skill, config, automation, or a programmatic surface when that is the smaller durable fix.

4. Use model and modality intentionally.
   - Default to GPT-5.5-family assumptions for high-quality prompt work: outcome-first goals, concise style controls, explicit evidence and stop rules, and measured reasoning effort.
   - Use fast/small models only for bounded text-first prompt tasks.
   - Do not assume text-agent prompting transfers cleanly to realtime, image generation, visual proof, or browser-state workflows.

## Workflow

1. Classify the prompt task:
   - fresh authoring
   - repair after an observed failure
   - critique of an existing prompt
   - workflow/surface design disguised as a prompt problem

2. Write or revise:
   - use only context that changes behavior
   - state the desired outcome before prescribing the process
   - state constraints and invariants once
   - give clear done-when criteria when execution is involved
   - specify output only as much as the consumer requires
   - include validation, retrieval budget, preamble, `phase`, or assistant-item replay rules only when the runtime needs them

3. Step back when needed:
   - If several prompt edits have failed, stop editing and diagnose the surrounding system.
   - If the fix depends on keyword heuristics or semantic prompt parsing, prefer a better Codex surface or tool contract.

## Reference

Load `references/prompt-patterns.md` when a concrete scaffold, prompt surgery checklist, or step-back meta prompt would help.

Load `references/gpt-5.5-prompting.md` when writing, migrating, or critiquing prompts for GPT-5.5, GPT-5 series reasoning models, Responses API agents, tool-heavy workflows, grounded retrieval, customer-facing assistants, or prompt stacks that may be over-specified for older models.

For GPT-5.5 or Responses API prompt work, default to the output shape in
`references/gpt-5.5-prompting.md`. Do not return only a revised prompt unless
the user explicitly asks for prompt-only output; include the diagnosis, runtime
contract, model/runtime settings, and validation plan so the prompt can be
evaluated rather than merely admired.

For substantial GPT-5.5 rewrites, make both layers skimmable:
- The response should include `Diagnosis`, `Runtime Contract`, `Revised Prompt`,
  `Model and Runtime Settings`, `Validation Plan`, and `Why This Is Better`.
  Do not replace these with looser labels like `Brief Explanation`,
  `Runtime Notes`, or `Recommended Settings`; use those only as subsections.
- The revised prompt should expose `Goal`, `Success criteria`, `Constraints`,
  `Runtime and tools`, `Output`, and `Stop rules`.
- The settings note should name `reasoning.effort`, `text.verbosity`, and any
  relevant Structured Outputs/schema, prompt caching, tool-description,
  preamble, or `phase` handling.
- The explanation should distinguish true invariants from judgment-call
  decision rules when repairing over-specified prompts.
- The validation plan should contain pass/fail eval checks for the revised
  prompt's observed failure mode, not just general advice.

If the user asks to "explain briefly" or "return the revised prompt plus
notes", keep the sections compact instead of dropping them. Brief still means
include:
- one diagnosis sentence,
- a settings line with `reasoning.effort` and `text.verbosity`,
- one or two validation/eval checks,
- the old absolute/process rules removed or converted, named concretely.

For migration tasks, explicitly name obsolete source-prompt rules that were
removed or converted. If the old prompt said "always search three times" or
"always use high reasoning", say that these were removed, replaced with a
retrieval budget, or converted into a setting to test.
