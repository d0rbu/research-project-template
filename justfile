# List the available development commands.
default:
    @just --list

# Install the locked environment and the local Git hooks.
setup:
    uv sync --locked
    uv run --locked pre-commit install --install-hooks

# Run the same complete gate as CI.
check:
    uv run --locked pre-commit run --all-files --show-diff-on-failure

# Verify that project metadata and the lockfile agree.
lock-check:
    uv lock --check

# Check Python style, imports, and annotations.
lint:
    uv run --locked ruff check .

# Apply safe lint fixes and format Python files.
fmt:
    uv run --locked ruff check --fix .
    uv run --locked ruff format .

# Check formatting without changing files.
format-check:
    uv run --locked ruff format --check .

# Check static types.
typecheck:
    uv run --locked ty check

# Find unused and unreachable Python code.
deadcode:
    uv run --locked vulture

# Run tests with coverage; additional pytest arguments are passed through.
[positional-arguments]
test *args:
    uv run --locked python -m pytest "$@"

# Generate a browsable coverage report under htmlcov/.
coverage:
    uv run --locked python -m pytest --cov-report=term-missing --cov-report=html

# Validate GitHub Actions workflow syntax, expressions, and action inputs.
workflow-check:
    uv run --locked actionlint

# Validate local Markdown link and image targets across the repository.
docs-check:
    uv run --locked python -m scripts.check_markdown_links
