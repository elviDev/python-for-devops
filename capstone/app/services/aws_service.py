from datetime import datetime, timedelta, timezone

import boto3
from botocore.exceptions import BotoCoreError, ClientError


def _get_s3_client():
    """Create a Boto3 S3 client using the active AWS credentials."""
    return boto3.client("s3")


def _get_ec2_client():
    """Create a Boto3 EC2 client for the configured AWS region."""
    return boto3.client("ec2")


def get_s3_report(days_threshold: int = 90) -> dict:
    """
    Return an inventory of S3 buckets grouped by age.

    Buckets older than the threshold are considered old.
    """
    if days_threshold < 0:
        raise ValueError("days_threshold cannot be negative")

    response = _get_s3_client().list_buckets()
    buckets = response.get("Buckets", [])

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days_threshold)

    new_buckets = []
    old_buckets = []

    for bucket in buckets:
        name = bucket["Name"]
        creation_date = bucket["CreationDate"]

        if creation_date < cutoff:
            old_buckets.append(name)
        else:
            new_buckets.append(name)

    return {
        "total_buckets": len(buckets),
        "new_buckets": new_buckets,
        "old_buckets": old_buckets,
        "age_threshold_days": days_threshold,
    }


def get_ec2_report() -> list[dict]:
    """Return EC2 instance IDs and their current states."""
    response = _get_ec2_client().describe_instances()

    instances = []

    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            instances.append(
                {
                    "instance_id": instance["InstanceId"],
                    "state": instance.get("State", {}).get("Name", "unknown"),
                }
            )

    return instances


def get_aws_report() -> dict:
    """Return a combined S3 and EC2 inventory report."""
    return {
        "s3": get_s3_report(),
        "ec2": get_ec2_report(),
    }