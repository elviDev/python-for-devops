from botocore.exceptions import BotoCoreError, ClientError
from fastapi import APIRouter, HTTPException

from app.services.aws_service import (
    get_aws_report,
    get_ec2_report,
    get_s3_report,
)


router = APIRouter(prefix="/aws", tags=["aws"])


@router.get("/s3")
def get_s3():
    """Return the S3 bucket inventory."""
    try:
        return get_s3_report()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except (BotoCoreError, ClientError) as exc:
        raise HTTPException(
            status_code=502,
            detail=f"AWS S3 error: {exc}",
        ) from exc


@router.get("/ec2")
def get_ec2():
    """Return the EC2 instance inventory."""
    try:
        return get_ec2_report()
    except (BotoCoreError, ClientError) as exc:
        raise HTTPException(
            status_code=502,
            detail=f"AWS EC2 error: {exc}",
        ) from exc


@router.get("/report")
def get_report():
    """Return the combined AWS resource inventory."""
    try:
        return get_aws_report()
    except (BotoCoreError, ClientError) as exc:
        raise HTTPException(
            status_code=502,
            detail=f"AWS error: {exc}",
        ) from exc