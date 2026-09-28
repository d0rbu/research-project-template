# Research Project Template

Correctness-first Python boilerplate for research projects.

The repository currently contains development tooling, executable correctness examples,
and documentation. Add a source package when there is real research code to organize.
Python 3.13 and a committed `uv.lock` keep the development environment reproducible.

## 1-minute quickstart

```bash
git clone https://github.com/d0rbu/research-project-template.git
cd research-project-template
uv sync --locked
uv run --locked pre-commit install
uv run --locked just check
```

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) first if needed;
it can install the Python version in `.python-version`. `just` is included in the
development dependencies, so a separate installation is optional.

## What this includes

| Area | Tooling |
|---|---|
| Package management | `uv`, `pyproject.toml`, `uv.lock` |
| Local commit checks | `pre-commit`, including file hygiene and lockfile validation |
| Linting and formatting | `ruff` |
| Type checking | `ty` |
| Tests | `pytest`, `pytest-cov`, `hypothesis`; 95% minimum coverage with branches |
| Dead code | `vulture` |
| Runtime contracts | `phantom-types`, `beartype` |
| Array shape/dtype checks | `jaxtyping` |
| Agent guidance | `AGENTS.md`, `CLAUDE.md` |
| Common commands | `justfile`, available through `uv run --locked just` |
| Automation | GitHub Actions runs the same gate; Dependabot proposes dependency updates |
| Workflow and docs checks | `actionlint` and an offline Markdown file-link checker |
| Merge policy | Pull requests and passing CI; reusable ruleset under `.github/rulesets/` |

Coverage currently measures maintenance commands in `scripts/` and executable examples
in `tests/`. Add the research source package when one exists; the current percentage
does not measure research code yet.

## Daily commands

```bash
uv run --locked just                          # list recipes
uv run --locked just fmt                      # fix lint and formatting
uv run --locked just test                     # tests and coverage
uv run --locked just test --no-cov -k weighted_mean  # focused tests
uv run --locked just check                    # full gate, also used by CI
```

The full gate checks the lockfile, Ruff lint and formatting, types, dead code, tests,
coverage, workflow semantics, local Markdown targets, JSON/YAML/TOML syntax, merge-conflict
markers, large added files, and whitespace. See [configuration](docs/reference/configuration.md)
for the local link check's scope and applying the merge ruleset to a new repository.

## Repo layout

```
tests/              pytest suite, including property tests
scripts/            tested repository maintenance commands
docs/               project documentation
.github/workflows/  CI checks
```

## Where to go next

| You want to... | Read |
|---|---|
| Navigate the documentation | [`docs/README.md`](docs/README.md) |
| Work as an agent | [`AGENTS.md`](AGENTS.md) |
| Start developing | [`docs/onboarding/getting-started.md`](docs/onboarding/getting-started.md) |
| Understand the correctness model | [`docs/development/correctness.md`](docs/development/correctness.md) |
| Write or debug tests | [`docs/development/testing.md`](docs/development/testing.md) |
| Add a new experiment | [`docs/pipelines/experiment-lifecycle.md`](docs/pipelines/experiment-lifecycle.md) |
| See tool configuration | [`docs/reference/configuration.md`](docs/reference/configuration.md) |
| Find a file's purpose | [`docs/reference/file-reference.md`](docs/reference/file-reference.md) |

## License

MIT. See [`LICENSE`](LICENSE).
