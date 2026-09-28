# Glossary

[Documentation index](../README.md) · [Correctness](../development/correctness.md) · [Configuration](../reference/configuration.md)

| Term | Meaning |
|---|---|
| Phantom type | A runtime primitive narrowed by a predicate and represented as a richer static type after validation. |
| Refinement function | A function such as `parse_probability` that validates raw input and returns a phantom type. |
| Runtime boundary | A place where untrusted values enter the system, such as CLI args, config files, data files, model outputs, or public APIs. |
| Property test | A Hypothesis test that checks an invariant across many generated examples. |
| Array contract | A dtype and shape expectation expressed with `jaxtyping` and enforced with `beartype`. |
| Lockfile | `uv.lock`, the resolved dependency graph used to recreate the environment. |
| Quality gate | The shared pre-commit checks required locally and in CI. |
| Branch coverage | Measurement of whether the possible paths through conditional code were exercised. |
| Dead-code analysis | Static analysis for unused or unreachable code, subject to dynamic-call false positives. |
| Recipe | A named command in the justfile, such as `check` or `test`. |
