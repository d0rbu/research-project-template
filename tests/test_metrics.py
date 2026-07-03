from __future__ import annotations

import numpy as np
import pytest
from hypothesis import given
from hypothesis import strategies as st
from jaxtyping import TypeCheckError

from research_template.metrics import normalize_weights, weighted_mean
from research_template.types import Probability


@pytest.mark.property
@given(
    st.lists(
        st.floats(min_value=1.0e-6, max_value=1.0e6, allow_nan=False, allow_infinity=False),
        min_size=1,
        max_size=32,
    )
)
def test_normalize_weights_returns_probability_vector(raw_weights: list[float]) -> None:
    weights = np.array(raw_weights, dtype=np.float64)

    normalized = normalize_weights(weights)

    assert normalized.dtype == np.float64
    assert normalized.shape == weights.shape
    assert np.all(normalized >= 0.0)
    assert float(np.sum(normalized)) == pytest.approx(1.0)


@pytest.mark.property
@given(
    st.lists(
        st.tuples(
            st.floats(min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False),
            st.floats(min_value=1.0e-6, max_value=1.0e6, allow_nan=False, allow_infinity=False),
        ),
        min_size=1,
        max_size=32,
    )
)
def test_weighted_mean_stays_in_probability_interval(pairs: list[tuple[float, float]]) -> None:
    values = np.array([value for value, _ in pairs], dtype=np.float64)
    weights = np.array([weight for _, weight in pairs], dtype=np.float64)

    result = weighted_mean(values, weights)

    assert isinstance(result, Probability)
    assert 0.0 <= result <= 1.0


def test_normalize_weights_rejects_zero_total() -> None:
    with pytest.raises(ValueError, match="positive"):
        normalize_weights(np.array([0.0, 0.0], dtype=np.float64))


def test_normalize_weights_rejects_empty_vector() -> None:
    with pytest.raises(ValueError, match="empty"):
        normalize_weights(np.array([], dtype=np.float64))


def test_normalize_weights_rejects_non_finite_values() -> None:
    with pytest.raises(ValueError, match="finite"):
        normalize_weights(np.array([1.0, np.nan], dtype=np.float64))


def test_normalize_weights_rejects_negative_values() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        normalize_weights(np.array([1.0, -0.5], dtype=np.float64))


def test_weighted_mean_rejects_shape_mismatch() -> None:
    with pytest.raises(TypeCheckError, match="weights"):
        weighted_mean(
            np.array([0.5, 0.25], dtype=np.float64),
            np.array([1.0], dtype=np.float64),
        )


def test_weighted_mean_rejects_non_probability_values() -> None:
    with pytest.raises(ValueError, match="probabilities"):
        weighted_mean(
            np.array([0.5, 1.5], dtype=np.float64),
            np.array([1.0, 1.0], dtype=np.float64),
        )
