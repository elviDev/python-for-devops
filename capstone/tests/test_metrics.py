from unittest.mock import patch

import pytest

from app.services.metrics_service import get_system_metrics


@patch("app.services.metrics_service.psutil.disk_usage")
@patch("app.services.metrics_service.psutil.virtual_memory")
@patch("app.services.metrics_service.psutil.cpu_percent")
def test_get_system_metrics(
    mock_cpu_percent,
    mock_virtual_memory,
    mock_disk_usage,
):
    mock_cpu_percent.return_value = 25.0
    mock_virtual_memory.return_value.percent = 50.0
    mock_disk_usage.return_value.percent = 40.0

    result = get_system_metrics()

    assert result == {
        "cpu_percentage": 25.0,
        "memory_percentage": 50.0,
        "disk_percentage": 40.0,
        "cpu_threshold": 85.0,
        "system_status": "Healthy",
    }


@patch("app.services.metrics_service.psutil.disk_usage")
@patch("app.services.metrics_service.psutil.virtual_memory")
@patch("app.services.metrics_service.psutil.cpu_percent")
def test_get_system_metrics_high_cpu(
    mock_cpu_percent,
    mock_virtual_memory,
    mock_disk_usage,
):
    mock_cpu_percent.return_value = 95.0
    mock_virtual_memory.return_value.percent = 50.0
    mock_disk_usage.return_value.percent = 40.0

    result = get_system_metrics()

    assert result["system_status"] == "High CPU"


def test_invalid_cpu_threshold():
    with pytest.raises(ValueError):
        get_system_metrics(cpu_threshold=101)

    with pytest.raises(ValueError):
        get_system_metrics(cpu_threshold=-1)