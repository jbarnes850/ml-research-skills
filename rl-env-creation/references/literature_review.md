# Literature Review Snapshot (May 2026)

This source map is for orienting environment-design decisions. Re-check sources when making public claims.

## Automated Environment Scaling
- Agent-World (arXiv 2604.18292): scales MCP-style environments by mining real-world themes, databases, and tools; synthesizes graph/programmatic verifiable tasks; uses held-out arena diagnosis for targeted task expansion. Key lesson: environment scale must be coupled to executable verification, difficulty control, and failure-driven refresh.
- EnvScaler (arXiv 2601.05808, GitHub RUC-NLPIR/EnvScaler): generates programmatic tool-interaction environments; uses LLM planning, Python environment classes, dual-agent assessment, and validator generation. Key lesson: black-box tool testing plus source/state checking is a minimum generated-environment gate.
- Agent World Model (arXiv 2602.10090, Snowflake repo/dataset): releases SQL-backed MCP environments with startup/tool tests, code-augmented judges, step-level protocol checks, and explicit environment-error handling. Key lesson: distinguish policy failure from environment/verifier failure.
- AutoForge (arXiv 2512.22857): generates state schemas, tools, DAG-based tasks, simulated users, and final-state rewards. Key lesson: simulated-user failures must be separated from agent failures.
- ScaleEnv (arXiv 2602.06820): emphasizes database/rule-level rewards and procedural tool testing, rejecting judge-only rewards for hackability. Key lesson: terminal-state verification beats sequence imitation or LLM-only judging.
- GUI-GENESIS (arXiv 2602.14093): synthesizes GUI environments with code-native reward assertions and dynamic self-verification. Key lesson: GUI tasks need stateful executable reward oracles, not only visual judges.
- Gym-Anything / CUA-World (arXiv 2604.06126): creates computer-use environments from real software with setup evidence, audit agents, task filtering, contamination graphs, and interface-use checks. Key lesson: generated envs need evidence packages and intended-interface audits.
- TRACE (arXiv 2604.05336): synthesizes capability-targeted micro-environments from failure traces and discards zero-variance rollout groups. Key lesson: targeted task refresh and reward-variance gates are central.

## Expert/Hand-Crafted Environment Research
- Surge CoreCraft / EnterpriseBench (arXiv 2602.16179): stateful e-commerce/customer-support world with thousands of entities, MCP tools, expert rubrics, train/held-out tasks, and OOD transfer claims. Key lesson: task quality, expert rubrics, and realistic workflow structure matter more than raw entity count.
- Surge Hierarchy of Agentic Capabilities (arXiv 2601.09032): identifies failure layers: tool use, planning, adaptability, groundedness, and common-sense reasoning. Key lesson: label tasks by capability axis and diagnose failures by layer.
- Surge Riemann-Bench (arXiv 2604.06802): private math tasks with independent expert verification and programmatic verifiers. Key lesson: high-stakes tasks need private held-out pools, independent solve checks, and verifier-backed uniqueness.
- Surge GDP.pdf / MMRB2 / AdvancedIF: multimodal and rubric-heavy evaluations. Key lesson: artifact-aware and criterion-level rubrics are required when scoring PDFs, images, instructions, or generated artifacts.
- BenchFlow SkillsBench/ClawsBench and BankerToolBench: Docker/MCP environments with trajectory capture, safety traps, per-criterion rewards, canaries, and artifact verifiers. Key lesson: report unsafe-action rate and leakage separately from task success.

## Reward Hacking, Leakage, and Task QA
- Reward Hacking Benchmark (arXiv 2605.02964): multi-step tool-use tasks instrumented for leakage, tampering, sequence manipulation, parser/proxy gaming, visible-check overfitting, and denial of evaluation; hardening sharply reduces exploits. Key lesson: success must be split into task success and integrity-clean success.
- Natural Emergent Misalignment from Reward Hacking in Production RL (arXiv 2511.18397): reward hacking learned in tool-using coding RL can generalize into broader misalignment; preventing hacking and diversifying safety training help. Key lesson: reward-hack probes are training blockers, not cosmetic evals.
- Reward Hacking in the Era of Large Models (arXiv 2604.13602): frames hacking as compressed objectives plus optimization amplification plus evaluator-policy co-adaptation. Key lesson: use decomposed rewards, bounded optimization, and evaluator hardening.
- Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv 2604.12086): models reward hacking under imperfect proxy rewards. Key lesson: when using proxies, track worst-case behavior and proxy/gold divergence.
- VerifyBench, BenchGuard, AgentHard, RHB-like works: stress verifier robustness, artifact quality, and hidden/invariant checks. Key lesson: verifiers must be tested under formatting, length, isomorphic variants, and adversarial tasks.

## Practical Principle
The current frontier is not "generate more environments." It is "generate or author environments, then admit only tasks whose world state, tool behavior, verifier, difficulty, leakage boundary, and exploit surface survive adversarial QA."
