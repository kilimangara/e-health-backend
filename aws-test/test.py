import boto3
import requests

def put_object():
    s3: boto3.client = boto3.client(
        service_name='s3',
        region_name='eu-north-1',
        aws_access_key_id='AKIAV44LYBIXFGPPXI6O',
        aws_secret_access_key='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'
    )

    response = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': 'emma-e-health-test',
            'Key': 'sh/sh.jpeg',
            'ContentMD5': 1 # важно
            # 'ContentType': 'image/jpeg', # важно в запросе передавать
            # 'ContentDisposition': 'attachment;filename={}'.format('clear.jpeg'), # важно в запросе передавать
        },
        ExpiresIn=3600,
    )

    print(f"curl -i --request PUT --upload-file images/clear.jpeg '{response}'")
    # print(response)

def get_object():
    s3: boto3.client = boto3.client(
        service_name='s3',
        region_name='eu-north-1',
        aws_access_key_id='AKIAV44LYBIXFGPPXI6O',
        aws_secret_access_key='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'
    )

    response = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': 'emma-e-health-test',
            'Key': 'sh/sh.jpeg',
            'ResponseContentType': 'image/jpeg', # важно в запросе передавать
            'ResponseContentDisposition': 'attachment;filename={}'.format('sgit.jpeg'), # важно в запросе передавать
            # 'Tags' :{}
        },
        ExpiresIn=3600,
        HttpMethod='GET',
    )

    res = requests.get(response)

    print(response)

def list_objects():
    s3 = boto3.client(
        service_name='s3',
        region_name='eu-north-1',
        aws_access_key_id='AKIAV44LYBIXFGPPXI6O',
        aws_secret_access_key='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'
    )

    # print(s3.list_objects(Bucket='emma-e-health-test'))
    for key in s3.list_objects_v2(Bucket='emma-e-health-test', Prefix='124817890571075')['Contents']:
        print(key)
        print(key['Key'])
    # buck = s3.bucket('emma-e-health-test')
    # print(buck.object.all())


if __name__ == '__main__':
    put_object()
