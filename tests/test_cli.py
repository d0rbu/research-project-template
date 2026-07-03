from __future__ import annotations

from research_template.cli import main


def test_main_prints_default_validation_fraction(capsys) -> None:
    main()

    assert capsys.readouterr().out == "validation_fraction=0.200\n"
