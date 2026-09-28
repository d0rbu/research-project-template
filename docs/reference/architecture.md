# Architecture

[Documentation index](../README.md) · [Correctness](../development/correctness.md) · [File reference](file-reference.md)

This repository is a compact, package-free scaffold for research projects. Tooling and examples are in place; research modules come next.

## Scaffold

The base repository intentionally starts without an importable source package. Add one
only when a research project has real reusable code.

| Module | Purpose |
|---|---|
| `tests/test_correctness_tools.py` | Executable examples for phantom types, runtime checks, array contracts, and property tests |
| `scripts/check_markdown_links.py` | Offline validation of local Markdown file and image targets |
| `tests/test_markdown_links.py` | Markdown parsing, file discovery, and rename regression tests |

## Correctness Boundary

Raw values should be refined near the boundary where they enter the system. Core code
should receive domain types such as `Probability`, not broad primitive values.

Array-heavy code should use `jaxtyping` for shape and dtype expectations and ordinary
runtime checks for semantic constraints such as non-negativity or finite values.

## Tests

`tests/` contains example tests and property tests. The default suite is intentionally
fast enough to run before every handoff.

## Adding the First Source Package

When reusable code arrives:

1. Create `src/your_project/` and move reusable logic there.
2. Add a build backend and change `tool.uv.package` so `uv sync` installs the package.
   Keep imports working through the installed package rather than editing `sys.path`.
3. Add the source package to `tool.coverage.run.source` alongside `scripts`, remove the
   scaffold `tests` target, and add the package name to
   Ruff's first-party import configuration. Ruff, ty, and Vulture already scan the root.
4. Keep test code under `tests/`, with focused examples and property tests for each
   public contract. Keep experiment orchestration separate from core functions.
5. Update this page and the [file reference](file-reference.md), then run the full gate.

## Tooling Flow

`uv.lock` determines the environment. The justfile exposes short development commands.
The pre-commit configuration owns the full gate, and both `just check` and GitHub
Actions invoke it. This keeps validation behavior consistent without duplicating a
second list of checks in CI. See the [configuration reference](configuration.md).

GitHub's merge rules are represented by `.github/rulesets/default-branch.json` and
applied through the repository settings API. File copies alone do not activate rulesets.
