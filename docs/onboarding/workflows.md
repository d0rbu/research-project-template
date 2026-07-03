# Workflows

## Add a Domain Type

1. Add the phantom type in `src/research_template/types.py`.
2. Add a `parse_*` refinement function for untrusted inputs.
3. Use the refined type in public functions and dataclasses.
4. Add `st.from_type(...)` property tests when the type has a Hypothesis strategy.
5. Update `docs/development/correctness.md` if the pattern is new.

## Add an Experiment Helper

1. Put reusable package code under `src/research_template/`.
2. Keep script-only orchestration out of core logic.
3. Validate raw inputs at the boundary.
4. Return typed values, dataclasses, or explicit result objects.
5. Cover invariants with unit tests and property tests.

## Before Handoff

```bash
uv run ruff check .
uv run ty check
uv run pytest
```

If a check is intentionally skipped, document the reason in the handoff.
