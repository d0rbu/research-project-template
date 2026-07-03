"""Tiny CLI used as an executable packaging smoke test."""

from __future__ import annotations

from research_template.experiment import ExperimentConfig, validation_fraction


def main() -> None:
    """Print a validated default split."""

    config = ExperimentConfig.from_raw(replicates=3, train_fraction=0.8)
    print(f"validation_fraction={validation_fraction(config):.3f}")
