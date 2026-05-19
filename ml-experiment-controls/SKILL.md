---
name: ml-experiment-controls
description: |
  Pattern for using control conditions to detect bugs in ML experiments.
  Use when: (1) designing ablation studies, (2) debugging unexpected baseline
  results, (3) a control condition underperforms the reference baseline.
  Explains why controls that SHOULD perform at least baseline are bug detectors,
  not just comparison points. Covers hypothesis separation and the
  format-vs-compression distinction.
---

# ML Experiment Controls as Bug Detectors

## Problem

When running ML experiments, control conditions are typically viewed as comparison
points. But they serve a more critical function: **controls that should perform
at or above baseline are bug detectors**. When they underperform, something is
wrong with the experimental setup, not the hypothesis.

## Context / Trigger Conditions

Use this knowledge when:

- A control condition performs significantly worse than expected
- Baseline results don't match known benchmarks
- You're debugging why an experiment "doesn't work"
- Designing experiments with multiple conditions
- Results seem too good or too bad to be true

**Warning signs of bugs, not effects:**
- Control that should match baseline is 10+ points worse
- Results contradict established literature
- Effect sizes are implausibly large
- Structured/formatted version underperforms flat version

## Solution

### The Control Hierarchy

| Control Type | Expected Performance | If Underperforms |
|--------------|---------------------|------------------|
| **Reference baseline** | Matches known benchmarks | Evaluation bug |
| **Equivalent transform** | = baseline (same info, different format) | Processing bug |
| **Additive condition** | >= baseline (same info + extra) | Implementation bug |
| **Experimental condition** | Unknown (what you're testing) | Actual result |

### Debugging Protocol

When a control underperforms:

1. **Stop the experiment** - Don't continue until resolved
2. **Compare inputs** - Look at what each condition actually receives
3. **Check for information loss** - Is the control dropping content?
4. **Verify processing** - Is formatting/rendering introducing artifacts?
5. **Fix and restart** - Clear traces, rerun from scratch

### Hypothesis Separation

Common mistake: conflating multiple hypotheses in one experiment.

**Example from Visual Session Encoding:**

| Hypothesis | Test Design |
|------------|-------------|
| "Visual FORMAT helps" | Same full content, visual vs text |
| "Visual COMPRESSION works" | Sampled content, measure accuracy retention |

The bug occurred when these were conflated: positional sampling (compression)
was applied to the format test, dropping answer-critical content. The control
(structured text with sampling) underperformed baseline by 26 points, revealing
the bug.

**Fix**: Phase 1 tests format with full content. Phase 2 tests compression only
after format is validated.

## Verification

After fixing a bug detected by controls:

1. Rerun the control condition
2. Verify it now performs at/above baseline
3. Only then interpret experimental conditions
4. Document what the control caught

## Example

**Scenario**: Visual session encoding experiment

**Initial Results**:

| Condition | Accuracy |
|-----------|----------|
| baseline_gemini | 84.4% |
| baseline_gemini_structured | 51.6% | ← **Bug signal** |
| visual | 47.2% |

**Investigation**: Structured text should be >= baseline (same information,
just formatted). A 26-point drop is impossible if content is identical.

**Root Cause**: Positional sampling (5 turns at 0%, 25%, 50%, 75%, 100%) was
applied to all conditions. For a session with 29 turns where the critical
answer was at position 3, the sampled indices [0, 7, 14, 21, 28] missed it.

**Fix**: Added `full_content=True` parameter to include all turns for format
testing. Compression testing deferred to Phase 2.

**Corrected Results**:

| Condition | Accuracy |
|-----------|----------|
| baseline_gemini | 84.4% |
| baseline_gemini_structured | 76.0% | ← Now reasonable (-8.4 pts from formatting overhead) |
| visual | 70.8% |

The control detected the bug before we drew incorrect conclusions about
visual encoding.

## Notes

### Information Asymmetry

When conditions have different information:
- You're testing WHAT information matters, not HOW it's presented
- Ensure baseline has same information as experimental conditions
- Log exactly what each condition receives

### Trace Everything

For debugging:
- Save full inputs to each condition
- Log intermediate processing steps
- Store reasoning traces, not just final answers
- Make comparison easy: side-by-side diffs

### Clear Before Rerun

When fixing bugs:
- Delete incomplete traces
- Restart experiments from scratch
- Don't mix pre-fix and post-fix results

## References

- Honcho Visual Session Encoding Experiment (Feb 2026) - Internal research
- [VTCBench](https://arxiv.org/abs/2512.15649) - Benchmark design with proper controls
