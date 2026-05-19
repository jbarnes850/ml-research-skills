# Problem Selection Framework

How to evaluate, select, and commit to research problems. Synthesized from
Hamming's "You and Your Research" (1986), Schulman's "Opinionated Guide to ML
Research," Sakana AI's research hiring guide (Druga, Darlow, Jones, 2026), and
the user's research context (RLVR, multilingual LLMs, curriculum engines).

## The Hamming Question

"What are the important problems of your field? What important problems are
you working on? If what you are working on is not important, and if you don't
think it is going to lead to something important, why are you working on it?"

Maintain a living document of the 3 most important open problems in each
subfield you touch. Revisit monthly. The list itself is a research artifact.

### Operationalizing "Important"

A problem is important when:
1. A solution would change how the community thinks or works
2. Multiple independent groups would build on the result
3. The result generalizes beyond the specific experimental setup
4. It addresses a bottleneck that blocks progress on downstream goals

A problem is *not* important merely because:
- It is technically hard
- It is trendy
- It has a clear metric to optimize
- Nobody has tried it yet

## Goal-Driven vs. Idea-Driven Research

### Idea-Driven (Schulman)
- Follow existing literature, incrementally improve methods
- Advantages: Low activation energy, clear baselines
- Drawbacks: High duplication risk, narrow contribution, less distinctive
  community perspective
- Best for: Early career, building technical depth in a specific area

### Goal-Driven (Schulman's recommendation)
- Define a capability gap or research vision
- Experiment across methods until one works
- Develop custom approaches that surpass existing solutions
- Advantages: Higher motivation, distinctive perspective, broader search
  space, less duplication
- Drawbacks: Higher risk of dead ends, requires broader knowledge

### Hybrid Approach (Recommended for mid-career researchers)
- Goal-driven direction, idea-driven tactics
- Set the long-term vision (e.g., "robust RLVR for multilingual reasoning")
- Within that vision, maintain idea-driven work on specific components
  (reward design, curriculum scheduling, evaluation methodology)

## The Selection Rubric

Score each candidate problem on three axes (1-5 scale):

### Impact (I)
- 1: Incremental improvement on well-explored method
- 2: Meaningful contribution within a subfield
- 3: Could change standard practice in a subfield
- 4: Opens a new research direction
- 5: Paradigm-level contribution (rare, high variance)

### Tractability (T)
- 1: No clear path; requires multiple breakthroughs
- 2: Plausible but requires 12+ months
- 3: Clear 6-month path with known risks
- 4: 3-month path with manageable risks
- 5: Achievable in weeks with existing infrastructure

### Personal Fit (F)
- 1: Requires expertise and infrastructure I don't have
- 2: Adjacent to my skills; significant ramp-up needed
- 3: Leverages some existing expertise
- 4: Strong alignment with current skills and infrastructure
- 5: Uniquely positioned; few others could execute this

### Composite Score

`Score = I * sqrt(T * F)`

Impact is multiplicative because a zero-impact problem with perfect
tractability is still worthless. Tractability and fit are under a square root
to prevent them from dominating -- a hard, high-impact problem should still
score well. A high-impact problem with moderate tractability beats a
low-impact problem that is easy to execute.

Warning: Do not over-index on tractability. Hamming explicitly warns against
choosing easy problems: "Great scientists tolerate ambiguity and accept
partial understanding as a temporary state."

## Worked Examples

### Example 1: Reward Design for Multilingual RLVR

- **Problem:** Current RLVR reward functions (code execution, math
  verification) don't generalize to languages without established formal
  verifiers.
- **Impact (4):** Opens RLVR to multilingual settings, a major bottleneck
  for non-English reasoning.
- **Tractability (3):** Can bootstrap from translation-based verification;
  unclear how noise propagates.
- **Personal Fit (5):** Directly leverages multilingual LLM and RLVR expertise.
- **Score:** 4 * sqrt(15) = 15.5

### Example 2: Kernel Optimization via RL

- **Problem:** Can RL discover CUDA kernel optimizations that outperform
  hand-tuned implementations?
- **Impact (3-4):** Practical value if it works; novel intersection of RL
  and systems.
- **Tractability (3):** Reward signal is well-defined (execution time), but
  search space is massive.
- **Personal Fit (4):** Active project, infrastructure exists.
- **Score:** 3.5 * sqrt(12) = 12.1

### Example 3: Scaling Laws for Curriculum Difficulty

- **Problem:** What is the optimal difficulty progression for RL-based
  training curricula as model scale increases?
- **Impact (3):** Would inform training recipes broadly.
- **Tractability (2):** Requires experiments at multiple scales; expensive.
- **Personal Fit (4):** Dynamical project directly addresses this.
- **Score:** 3 * sqrt(8) = 8.5

## Commitment and Pivoting

### The 3-Month Rule

Commit to a research direction for at least 3 months before evaluating
whether to pivot. Shorter timelines don't allow enough depth for the
approach to succeed or fail definitively.

### Pivot Signals (from hypothesis-framework.md)
- Three consecutive null results on the core hypothesis
- Estimated remaining compute exceeds budget by 3x
- Competing group publishes strictly better approach
- Problem importance decreased (field shifted)

### Do Not Pivot When
- A single experiment fails (debug first)
- Results are noisy but trending correctly
- A reviewer rejected a paper (address feedback, iterate)

### Schulman's Strategic Problem-Switching
- Identify dead-end indicators early
- Commit to completion; avoid excessive switching
- When genuinely stuck, table the problem and return with fresh perspective
  (Hamming: "The prepared mind" catches insights across domains)
- "Switching problems too frequently (and giving up on promising ideas) is a
  more common failure mode than not switching enough."
- Retrospective test: Look back over months. If substantial time went to
  half-finished projects abandoned for newer ideas, strengthen follow-through.

### Schulman's Case Study: Locomotion to PPO

During Schulman's PhD, he chose 3D humanoid locomotion as a concrete goal.
When DeepMind published DQN on Atari, many researchers jumped to Q-learning.
Schulman had already explored Q-learning and found it unsuitable for
locomotion -- so he continued with policy gradients, producing TRPO, GAE,
and eventually PPO.

Key lesson: **Choosing a different problem from the crowd leads to exploring
different ideas.** Goal-driven research provides differentiated perspective
that idea-driven research cannot.

### The Complexity/Improvement Ratio (Schulman)

"If your idea gives a 10% improvement, it better be 2 lines of code.
If it gives a 50% improvement, it can add 10 lines."

Incremental improvements are useful only in the context of a larger goal.
The standalone value of an increment scales inversely with its complexity.
A method that slightly improves on baseline must be trivially simple,
or no one will adopt it.

## Reframing: Defects as Assets

Hamming's principle: What appears to be a defect may be an asset when
reframed.

- "The machine can't do X" -> "What if the constraint forces a better
  solution?"
- "This reward is too noisy" -> "What if noise *is* the curriculum signal?"
- "This model is too small" -> "What if small-scale phenomena predict
  large-scale behavior?"

Practice inverting constraints. The best research questions often come from
treating a limitation as a feature.

## Personal Development as Research Infrastructure

### Schulman's Knowledge-Building Protocol

1. **Textbooks over papers for foundational knowledge.** "Most students of
   machine learning don't spend time reading textbooks after they finish their
   school courses. I think this is a mistake, since textbooks are a much more
   dense way to absorb knowledge than papers." Choose a small set of relevant
   textbooks and work through them gradually.

2. **PhD theses as literature reviews.** Parts (1) introduction and (3)
   conclusion of theses contain "a unifying view of the past and future of
   the field, written by an expert." Often the best literature review of an
   active area.

3. **Reimplementation before extension.** "Reimplementing ideas from papers
   gives a much deeper understanding than passive reading. Once you can easily
   reproduce the state-of-the-art, you'll be ready to go beyond it."

4. **Critical paper reading at scale.** Skim incoming papers to notice trends
   and observe the dependency graph of ideas -- which ideas become widely used,
   which are forgotten.

5. **Active effort to escape comfort zones.** "Your knowledge is likely to
   plateau after you learn the basics that you need for your day-to-day work.
   You may need to expend active effort to expand this zone."

### The Research Notebook (Schulman)

- Create daily entries: ideas, experiments, results (plots, tables)
- Every 1-2 weeks: review and condense into summary with sections for
  experimental findings, insights, code progress, next steps
- During review: check if previous week's ideas were followed up
- Transfer backburner ideas to a separate list
- Monitor time allocation: are months going to half-finished projects?

### Prediction Training for Taste

Research taste improves faster when decisions become labeled datapoints:

- Before asking a mentor or collaborator, predict their recommendation and the
  reason they will give.
- Before reading a paper's experiments, predict the method choices, likely
  failure modes, and what result would make the paper matter.
- Before launching a project phase, write the expected result and the evidence
  that would make you stop.
- During weekly review, compare predictions to outcomes. Separate misses caused
  by execution bugs from misses caused by bad judgment about the problem.

The goal is not self-criticism. The goal is to collect supervised data for the
parts of research taste that otherwise have slow feedback loops.

## Annual Research Taste Audit

Once per year, review:

1. Which of my past projects had lasting impact? What made them different?
2. Which papers from my field were I initially skeptical of, but turned out
   to be important? What does this reveal about my blind spots?
3. Which ideas prospered and which were forgotten? What distinguishes them?
4. Am I working on problems that matter, or problems that are comfortable?
5. What would I work on if I had unlimited compute and a guaranteed 3 years?
