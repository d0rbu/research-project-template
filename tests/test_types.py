from __future__ import annotations

import pytest
from hypothesis import given
from hypothesis import strategies as st

from research_template.experiment import ExperimentConfig, validation_fraction
from research_template.types import (
    PositiveCount,
    Probability,
    parse_positive_count,
    parse_probability,
)


@pytest.mark.property
@given(st.from_type(Probability))
def test_probability_strategy_generates_valid_values(value: Probability) -> None:
    assert isinstance(value, Probability)
    assert 0.0 <= value <= 1.0


@pytest.mark.property
@given(st.from_type(PositiveCount))
def test_positive_count_strategy_generates_valid_values(value: PositiveCount) -> None:
    assert isinstance(value, PositiveCount)
    assert value > 0


@pytest.mark.parametrize("raw", [-0.1, 1.1, "not-a-float"])
def test_probability_rejects_invalid_values(raw: float | str) -> None:
    with pytest.raises((TypeError, ValueError)):
        parse_probability(raw)


@pytest.mark.parametrize("raw", [0, -1, "not-an-int"])
def test_positive_count_rejects_invalid_values(raw: int | str) -> None:
    with pytest.raises((TypeError, ValueError)):
        parse_positive_count(raw)


def test_experiment_config_refines_untrusted_values() -> None:
    config = ExperimentConfig.from_raw(replicates="3", train_fraction="0.75")

    assert isinstance(config.replicates, PositiveCount)
    assert isinstance(config.train_fraction, Probability)
    assert validation_fraction(config) == pytest.approx(0.25)
