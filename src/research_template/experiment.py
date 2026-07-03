"""Experiment configuration primitives."""

from __future__ import annotations

from dataclasses import dataclass

from beartype import beartype

from research_template.types import (
    PositiveCount,
    Probability,
    parse_positive_count,
    parse_probability,
)


@dataclass(frozen=True, slots=True)
class ExperimentConfig:
    """Minimal validated experiment configuration."""

    replicates: PositiveCount
    train_fraction: Probability

    @classmethod
    def from_raw(cls, *, replicates: int | str, train_fraction: float | int | str) -> ExperimentConfig:
        """Build a config from untrusted primitive values."""

        return cls(
            replicates=parse_positive_count(replicates),
            train_fraction=parse_probability(train_fraction),
        )


@beartype
def validation_fraction(config: ExperimentConfig) -> Probability:
    """Return the held-out fraction implied by a train fraction."""

    return parse_probability(1.0 - config.train_fraction)
