# Environment Scaling Patterns

## Hand-Crafted Expert World
Use when realism, policy constraints, edge cases, and reward validity dominate scale.

Required properties:
- Task-centric world building: entities and tools exist to support diverse, challenging tasks.
- Expert-authored tasks and rubrics.
- Stateful tools with replayable trajectories.
- Held-out eval tasks and, for public claims, private or refreshed tasks.
- Capability-axis labels and failure taxonomy.

Best for: enterprise workflows, customer support, banking, math/science tasks, multimodal document tasks, safety/authorization environments.

Common failure: maximizing entity/tool count while tasks remain redundant, trivial, or weakly verified.

## Programmatic or Generated World
Use when the goal is breadth across many tool-interaction sandboxes.

Required properties:
- Explicit generator inputs: task source, theme source, tool docs, database source, or MCP/server metadata.
- Generated world model with executable tools, not only text simulation.
- Compile/unit-test filtering for tools.
- Task generation through executable traces, reference solutions, or verifier code.
- Admission filters for solvability, ambiguity, difficulty, and exploitability.

Best for: large-scale tool-use corpora, synthetic MCP-style environments, data-processing tasks, and capability-gap refresh loops.

Common failure: treating generated volume as quality while the verifier checks only schemas or visible outputs.

## Hybrid World
Use when scale and realism are both needed.

Required properties:
- Generated breadth for candidate environments/tasks.
- Expert or adversarial admission for high-value task families.
- Stratified difficulty and capability coverage.
- Private held-out tasks from a separate generation/review path.
- Ongoing diagnosis loop: failures on held-out tasks drive targeted new tasks, not blind expansion.

## Scaling Loop
1. Build candidate worlds/tasks.
2. Filter tools/verifiers by compile, unit, and replay tests.
3. Admit tasks with solvability and difficulty evidence.
4. Run adversarial integrity probes.
5. Train only on admitted training split.
6. Evaluate on held-out and private/refresh tasks.
7. Diagnose capability gaps from trajectories.
8. Generate or author targeted new tasks.

Do not collapse steps 3 and 4 into the generator prompt. They are separate gates.
