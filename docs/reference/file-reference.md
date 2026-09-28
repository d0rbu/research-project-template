# File Reference

[Documentation index](../README.md) · [Architecture](architecture.md) · [Configuration](configuration.md)

## Top Level

| File | Purpose |
|---|---|
| `README.md` | Project summary, quickstart, and doc links |
| `AGENTS.md` | Agent entry point and repo conventions |
| `CLAUDE.md` | Claude-specific pointer to agent conventions |
| `pyproject.toml` | Package metadata and tool configuration |
| `uv.lock` | Locked dependency graph |
| `.pre-commit-config.yaml` | Shared gate for Python tooling, workflow semantics, local Markdown targets, justfile syntax, and file hygiene |
| `justfile` | Setup, checks, formatting, types, dead code, tests, coverage, workflow, and docs commands |
| `.python-version` | Python version for local tooling |
| `.gitignore` | Local artifacts excluded from git |
| `.editorconfig` | Editor defaults for encoding, indentation, whitespace, and line endings |
| `LICENSE` | MIT license |

## Tests

| File | Purpose |
|---|---|
| `tests/test_correctness_tools.py` | Phantom types, validated parsing, stable normalization, runtime array contracts, and property/regression tests |
| `tests/test_markdown_links.py` | File/link semantics and Git-discovery regression tests for the Markdown checker |

## Maintenance Commands

| File | Purpose |
|---|---|
| `scripts/__init__.py` | Importable namespace for repository tools |
| `scripts/check_markdown_links.py` | Offline check for local Markdown file and image targets across tracked and new documents |

## Docs

| Path | Purpose |
|---|---|
| `docs/README.md` | Documentation index |
| `docs/onboarding/getting-started.md` | Prerequisites, locked setup, and first checks |
| `docs/onboarding/workflows.md` | Change types, code, dependencies, and prepare a handoff |
| `docs/onboarding/glossary.md` | Shared correctness and tooling vocabulary |
| `docs/development/correctness.md` | Refinement types, runtime contracts, numeric validation, and static analysis |
| `docs/development/testing.md` | Test strategy, selection, strictness, and coverage interpretation |
| `docs/pipelines/experiment-lifecycle.md` | From a research question to reproducible outputs |
| `docs/reference/architecture.md` | Current layout and introducing the first source package |
| `docs/reference/configuration.md` | Tool settings, hook ownership, recipes, and CI |
| `docs/reference/file-reference.md` | This file map; update it when file roles change |

## CI

| File | Purpose |
|---|---|
| `.github/workflows/ci.yml` | Runs the shared pre-commit gate on main pushes, pull requests, and manual dispatch |
| `.github/dependabot.yml` | Weekly grouped uv and GitHub Actions dependency update proposals |
| `.github/rulesets/default-branch.json` | Portable PR and required-CI policy, applied separately to each GitHub repository |
