from typing import Dict, List

import boto3

from app.core.config import settings
from app.db.models.image import ImageBlobDBModel


def generate_upload_urls(data: List[ImageBlobDBModel]) -> Dict:
    result = {}

    client = get_client()

    for image in data:
        url = client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": settings.AMAZON_BUCKET_NAME,
                "Key": image.filename,
                "ContentMD5": image.check_sum,
                "ContentLength": image.byte_size,
            },
            ExpiresIn=3600,
        )
        result[image.id] = url

    return result


def generate_download_url(filename, content_type):
    if filename is None or content_type is None:
        return None

    client = get_client()

    return client.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": settings.AMAZON_BUCKET_NAME,
            "Key": filename,
            "ResponseContentType": content_type,
        },
        ExpiresIn=3600,
        HttpMethod="GET",
    )


def get_client() -> boto3.client:
    """Получение клиента для амазона."""
    return boto3.client(
        service_name=settings.AMAZON_SERVICE_NAME,
        region_name=settings.AMAZON_REGION_NAME,
        aws_access_key_id=settings.AMAZON_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AMAZON_SECRET_ACCESS_KEY,
    )
