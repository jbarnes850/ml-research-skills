# Annotated Sources

Curated bibliography for the ML Research Design skill. Each entry includes
the core insight relevant to the seven pillars framework.

## Primary Sources

### Sakana AI -- An Unofficial Guide to Prepare for a Research Position Application (2026)
- **Authors:** Stefania Druga, Luke Darlow, Llion Jones
- **URL:** https://pub.sakana.ai/Unofficial_Guide/
- **Core insight:** "The single biggest differentiator between successful and
  unsuccessful candidates isn't whether they completed the technical assessment,
  it's whether they understand what they built, and are able to clearly explain
  their understanding."
- **Key contributions to pillars:**
  - Pillar 2: Minimum viable experiment methodology
  - Pillar 3: "Depth over breadth" as explicit principle
  - Pillar 4: Understanding over implementation
  - Pillar 5: Clarity of communication
  - Pillar 6: "Good enough is good enough" and actionability test
  - Pillar 7: Intuition development through hands-on building
- **2026 context:** "In 2026 it is surprisingly easy to seem creative and to
  have good ideas. However, ideas that remain unactionable are worthless."

### John Schulman -- An Opinionated Guide to ML Research (2017, OpenAI Fellows)
- **URL:** http://joschu.net/blog/opinionated-guide-ml-research.html
- **Core insight:** "Your ability to choose the right problems to work on is
  even more important than your raw technical skill."
- **Key contributions to pillars:**
  - Pillar 1: Goal-driven > idea-driven research; case study of locomotion
    -> TRPO -> GAE -> PPO showing how goal-driven perspective avoids herd
    behavior (he ignored the DQN/Atari bandwagon because it didn't serve
    his locomotion goal)
  - Pillar 1: "To make breakthroughs with idea-driven research, you need to
    develop an exceptionally deep understanding of your subject, and a
    perspective that diverges from the rest of the community"
  - Pillar 1: Restrict to general solutions: "constrain your search to
    solutions that seem general and can be applied to other problems"
  - Pillar 3: Daily notebooks, bi-weekly reviews, backburner idea lists
  - Pillar 4: Textbooks > papers for foundational knowledge; reimplement
    algorithms from primary sources before extending
  - Pillar 6: Epsilon-greedy exploration budget (1 day/week on divergent ideas)
  - Pillar 7: "Watch which ideas prosper and which ones are forgotten...
    which serve as building blocks and which are ignored because too
    complicated, too fragile, or the improvement too small"
- **Framework:** Three pillars of success: right problems, continual progress,
  personal growth
- **On switching problems:** "Switching problems too frequently is a more
  common failure mode than not switching enough"
- **Complexity/improvement ratio:** "If it gives a 10% improvement, it better
  be 2 lines of code, whereas if it's a 50% improvement, it can add 10 lines"

### Richard Hamming -- You and Your Research (1986)
- **URL:** https://www.cs.virginia.edu/~robins/YouAndYourResearch.html
- **Core insight:** "If you do not work on an important problem, it's unlikely
  you'll do important work."
- **Key contributions to pillars:**
  - Pillar 1: The Hamming question (what are the important problems?)
  - Pillar 7: "Luck favors the prepared mind"
  - Problem-selection: Reframing defects as assets
- **Enduring relevance:** The talk is from 1986 but the principles about
  problem selection, courage to work on hard problems, and the relationship
  between preparation and luck remain the most cited research methodology
  framework in CS.

### Andrej Karpathy -- A Recipe for Training Neural Networks (2019)
- **URL:** https://karpathy.github.io/2019/04/25/recipe/
- **Core insight:** "The most common neural net mistakes aren't errors in
  the math or bugs in the code. They're silent failures." Training requires
  "patience and attention to detail" as success correlates most strongly with
  these qualities.
- **Key contributions to pillars:**
  - Pillar 2: Six-stage systematic ladder (data -> baseline -> overfit ->
    regularize -> tune -> squeeze)
  - Pillar 3: "Become one with the data"
  - Pillar 7: Silent failures demand methodical verification
- **Methodology:** Build from simple to complex. Verify every assumption.
  Never introduce unverified complexity simultaneously. Visualize before
  and during training.

## Complementary Sources (2025-2026)

### Microsoft Research -- Inside the Edge of Discovery: What Will Shape AI in 2026
- **URL:** https://www.microsoft.com/en-us/research/story/whats-next-in-ai/
- **Relevant insights:**
  - AI evolving from tool to research companion; persistent memory enables
    stabilizing research partnership
  - Start with hardest use cases, not average ones (Tanuja Ganu)
  - Multi-modal integration across formerly siloed modalities
  - Simulation and stress-testing as early methodology before deployment
  - Physical intelligence and embodied models as next frontier

### AI for Science 2025 (Nature)
- **URL:** https://www.nature.com/articles/d42473-025-00161-3
- **Relevant insights:**
  - AI integrating data-driven modeling with prior knowledge
  - Automating hypothesis generation and validation
  - Human researchers retain critical oversight: curating datasets, designing
    reward functions, interpreting AI-generated hypotheses with skepticism

### RLHF Comprehensive Survey (2025)
- **URL:** https://arxiv.org/abs/2504.12501
- **Relevant insights:**
  - Online Iterative RLHF for continuous adaptation
  - RLVR (Reinforcement Learning with Verifiable Rewards) as shift from
    subjective to objective alignment
  - RLTHF (Targeted Human Feedback) for annotation efficiency

### From Hypothesis to Publication: AI-Driven Research Support Systems (2025)
- **URL:** https://arxiv.org/html/2503.01424v1
- **Relevant insights:**
  - Comprehensive survey of how AI tools support each stage of the
    research pipeline
  - Emphasis on maintaining methodological rigor alongside AI acceleration
  - FAIR compliance and systematic data curation as universal standards

## Thematic Bibliography

### On Research Taste
- Schulman's guide (above) -- most practical treatment
- Hamming's talk (above) -- most philosophical treatment
- Sakana (above) -- most actionable in 2026 AI context

### On Systematic Experimentation
- Karpathy's recipe (above) -- gold standard for neural net debugging
- User's own CLAUDE.md staged validation ladder -- operationalized for
  GPU compute

### On Problem Selection
- Hamming (above) -- the foundational framework
- Schulman (above) -- goal-driven vs. idea-driven distinction
- Sakana (above) -- "Did I solve the right problem, or just a problem?"

### On Communication
- Sakana (above) -- "Clarity isn't about saying more"
- User's writing-style.md -- first-person singular, declarative, evidence-first

### On the 2026 Research Landscape
- Microsoft Research (above) -- multi-modal, agentic, embodied directions
- Nature AI for Science (above) -- AI as hypothesis generator
- RLHF survey (above) -- RLVR and verifiable alignment trajectory
