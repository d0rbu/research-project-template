# Architecture

This repository is a compact Python package template for research code.

## Package

`src/research_template/` contains reusable code.

| Module | Purpose |
|---|---|
| `types.py` | Domain phantom types and refinement functions |
| `experiment.py` | Validated experiment configuration primitives |
| `metrics.py` | Metric helpers with array shape and dtype contracts |
| `cli.py` | Minimal executable smoke-test CLI |

## Correctness Boundary

Raw values should be refined near the boundary where they enter the system. Core code
should receive domain types such as `Probability` and `PositiveCount`, not broad
primitive values.

Array-heavy code should use `jaxtyping` for shape and dtype expectations and ordinary
runtime checks for semantic constraints such as non-negativity or finite values.

## Tests

`tests/` contains example tests and property tests. The default suite is intentionally
fast enough to run before every handoff.
