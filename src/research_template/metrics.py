"""Small metric helpers that demonstrate runtime array contracts."""

from __future__ import annotations

import numpy as np
from beartype import beartype
from jaxtyping import Float64, jaxtyped

from research_template.types import Probability, parse_probability

Vector = Float64[np.ndarray, "n"]


@jaxtyped(typechecker=beartype)
def normalize_weights(weights: Vector) -> Vector:
    """Normalize a non-empty vector of finite, non-negative weights."""

    if weights.size == 0:
        raise ValueError("weights must not be empty")
    if not np.all(np.isfinite(weights)):
        raise ValueError("weights must be finite")
    if np.any(weights < 0):
        raise ValueError("weights must be non-negative")

    total = float(np.sum(weights))
    if total <= 0.0:
        raise ValueError("at least one weight must be positive")

    return weights / total


@jaxtyped(typechecker=beartype)
def weighted_mean(values: Vector, weights: Vector) -> Probability:
    """Compute a weighted mean of values already known to be probabilities."""

    if np.any((values < 0.0) | (values > 1.0)):
        raise ValueError("values must be probabilities")

    normalized = normalize_weights(weights)
    result = float(np.dot(values, normalized))
    return parse_probability(min(1.0, max(0.0, result)))
