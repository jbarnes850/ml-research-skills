# Telemetry Hygiene (Single-Run Policy)

## Goal
Ensure a single writer per run to avoid non-monotonic steps and duplicated metrics.

## Recommendations
- Disable trainer-level W&B logging if you already log per-episode metrics.
- Use a unique run name per training job; never reuse run IDs across restarts.
- On resume, either continue the same run with strict step ordering or start a new run cleanly.

## Preflight checks
- Confirm WANDB_API_KEY is set before training.
- Validate that only one process initializes W&B.
- Verify step count increases monotonically in logs.
