from unittest.mock import patch

import pytest

from app.routers.ai import resolve_log_path


def test_resolve_default_log():
    path = resolve_log_path(None)

    assert path.name == "app.log"
    assert path.suffix == ".log"


def test_resolve_valid_log():
    path = resolve_log_path("app.log")

    assert path.name == "app.log"


def test_reject_absolute_path():
    with pytest.raises(ValueError):
        resolve_log_path("C:\\Windows\\System32\\secret.log")


def test_reject_path_traversal():
    with pytest.raises(ValueError):
        resolve_log_path("../../secret.log")


def test_reject_non_log_file():
    with pytest.raises(ValueError):
        resolve_log_path("notes.txt")


@patch("app.routers.ai.analyze_logs_with_ai")
def test_ai_router_uses_resolved_path(mock_analyze):
    mock_analyze.return_value = {
        "log_file": "sample_logs\\app.log",
        "counts": {
            "INFO": 10,
            "WARNING": 2,
            "ERROR": 3,
        },
        "analysis": "Test analysis",
        "model": "qwen3.6:latest",
    }

    from app.routers.ai import analyze_with_ai
    from app.schemas.ai import AIAnalyzeRequest

    response = analyze_with_ai(
        AIAnalyzeRequest(file="app.log")
    )

    assert response["counts"]["ERROR"] == 3
    mock_analyze.assert_called_once()