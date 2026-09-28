# Experiment Lifecycle

[Documentation index](../README.md) · [Workflows](../onboarding/workflows.md) · [Correctness](../development/correctness.md)

Use this as the default lifecycle when research implementation begins.

## 1. Define the Question

Write down the hypothesis, metric, and expected failure modes before adding code.
State which data split and baseline the comparison uses.

## 2. Make State Explicit

Represent raw config as validated dataclasses. Use phantom types for values that have
domain bounds such as probabilities, positive counts, feature IDs, seeds, and split
fractions.

## 3. Build Small Reusable Units

Keep reusable logic in a real module once the project has source code. Keep one-off
orchestration in scripts or notebooks that call reusable code.

## 4. Test Invariants

Add example tests for known cases and property tests for broad invariants.
Choose numerical tolerances that match the computation and document why they are
appropriate. Follow the [testing guide](../development/testing.md) for the full gate.

## 5. Record Outputs

Keep generated artifacts out of git by default. Put durable notes in docs or experiment
reports, and make artifact paths explicit.

Record the code revision, configuration, random seed, dependency lockfile identity,
dataset/model identity, and output location. Distinguish a configured or running
experiment from completed, validated results. Add experiment-specific docs when there
is a concrete protocol to describe.
