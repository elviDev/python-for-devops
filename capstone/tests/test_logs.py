from pathlib import Path

import pytest

from app.services.log_service import analyze_log_file, count_log_levels


def test_count_log_levels():
    text = """
    INFO Application started
    WARNING High memory usage
    ERROR Database timeout
    """

    assert count_log_levels(text) == {
        "INFO": 1,
        "WARNING": 1,
        "ERROR": 1,
    }


def test_count_log_levels_does_not_match_partial_words():
    text = "INFO No errors were found."

    assert count_log_levels(text) == {
        "INFO": 1,
        "WARNING": 0,
        "ERROR": 0,
    }


def test_analyze_log_file():
    log_file = Path(__file__).parents[1] / "sample_logs" / "app.log"

    result = analyze_log_file(log_file)

    assert result["total_lines"] > 0
    assert result["counts"]["INFO"] > 0
    assert result["counts"]["WARNING"] > 0
    assert result["counts"]["ERROR"] > 0


def test_missing_log_file():
    with pytest.raises(FileNotFoundError):
        analyze_log_file("does-not-exist.log")