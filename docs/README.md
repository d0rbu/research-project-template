# Documentation

Start with the [project README](../README.md) or [agent guide](../AGENTS.md).
These docs are the source of truth for this repository. Keep top-level files short and
update these documents when behavior, commands, or layout changes.

For a first visit, follow getting started → workflows → correctness → testing. Use the
reference section for exact configuration and file ownership. Each page links back here
and to related guidance. Extend this small hierarchy as the implementation grows.

Run `uv run --locked just docs-check` after moving or editing documentation. The full
gate checks all local Markdown file and image targets, including links in unchanged files.

## Onboarding

- [`onboarding/getting-started.md`](onboarding/getting-started.md) - local setup
- [`onboarding/workflows.md`](onboarding/workflows.md) - common development flows
- [`onboarding/glossary.md`](onboarding/glossary.md) - project vocabulary

## Development

- [`development/correctness.md`](development/correctness.md) - how to use phantom
  types, runtime checks, array contracts, and property tests
- [`development/testing.md`](development/testing.md) - test strategy and commands

## Pipelines

- [`pipelines/experiment-lifecycle.md`](pipelines/experiment-lifecycle.md) - a reusable
  lifecycle for research experiments

## Reference

- [`reference/architecture.md`](reference/architecture.md) - current layout and adding a source package
- [`reference/configuration.md`](reference/configuration.md) - tool configuration
- [`reference/file-reference.md`](reference/file-reference.md) - file-by-file map

## Maintaining the docs

Put durable knowledge in the page that owns it and link to it from related pages.
Update the file reference when adding or changing a file's role. Add new sections only
when there is concrete code or a decision to document. Commands must work from the
repository root, and validation claims should say what was actually checked.
