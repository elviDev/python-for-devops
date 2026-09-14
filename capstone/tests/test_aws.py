from unittest.mock import MagicMock, patch

import pytest

from app.services.aws_service import get_ec2_report, get_s3_report


@patch("app.services.aws_service._get_s3_client")
def test_get_s3_report(mock_get_client):
    mock_client = MagicMock()

    mock_client.list_buckets.return_value = {
        "Buckets": [
            {
                "Name": "new-bucket",
                "CreationDate": __import__("datetime").datetime.now(
                    __import__("datetime").timezone.utc
                ),
            }
        ]
    }

    mock_get_client.return_value = mock_client

    result = get_s3_report(days_threshold=90)

    assert result["total_buckets"] == 1
    assert result["new_buckets"] == ["new-bucket"]
    assert result["old_buckets"] == []


@patch("app.services.aws_service._get_ec2_client")
def test_get_ec2_report(mock_get_client):
    mock_client = MagicMock()

    mock_client.describe_instances.return_value = {
        "Reservations": [
            {
                "Instances": [
                    {
                        "InstanceId": "i-1234567890",
                        "State": {"Name": "running"},
                    }
                ]
            }
        ]
    }

    mock_get_client.return_value = mock_client

    result = get_ec2_report()

    assert result == [
        {
            "instance_id": "i-1234567890",
            "state": "running",
        }
    ]


def test_invalid_s3_age_threshold():
    with pytest.raises(ValueError):
        get_s3_report(days_threshold=-1)