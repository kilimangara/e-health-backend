from typing import Dict, List

import boto3

from app.db.models.image import ImageBlob


def generate_upload_urls(data: List[ImageBlob]) -> Dict:
    result = {}

    s3: boto3.client = boto3.client(
        service_name="s3",
        region_name="eu-north-1",
        aws_access_key_id="AKIAV44LYBIXFGPPXI6O",
        aws_secret_access_key="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",
    )

    for image in data:
        url = s3.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": "emma-e-health-test",
                "Key": image.filename,
                "ContentMD5": image.check_sum,
            },
            ExpiresIn=3600,
        )
        result[image.id] = url

    return result
