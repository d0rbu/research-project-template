"""Domain-specific phantom types.

Phantom types let us keep the runtime representation simple while exposing a narrower
type to static and runtime checkers after validation.
"""

from __future__ import annotations

from typing import Any

from phantom import Phantom


def _is_probability(value: float) -> bool:
    return 0.0 <= value <= 1.0


def _is_positive_count(value: int) -> bool:
    return type(value) is int and value > 0


class Probability(float, Phantom[float], predicate=_is_probability, bound=float):
    """A float value in the closed interval [0, 1]."""

    @classmethod
    def __register_strategy__(cls) -> Any:
        from hypothesis import strategies as st

        return st.floats(min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False)


class PositiveCount(int, Phantom[int], predicate=_is_positive_count, bound=int):
    """An integer count that must be strictly positive."""

    @classmethod
    def __register_strategy__(cls) -> Any:
        from hypothesis import strategies as st

        return st.integers(min_value=1)


def parse_probability(value: float | int | str) -> Probability:
    """Validate and refine a raw value into a probability."""

    raw = float(value) if isinstance(value, str | int) else value
    return Probability.parse(raw)


def parse_positive_count(value: int | str) -> PositiveCount:
    """Validate and refine a raw value into a positive count."""

    raw = int(value) if isinstance(value, str) else value
    return PositiveCount.parse(raw)
