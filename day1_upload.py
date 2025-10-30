import boto3
from dotenv import load_dotenv
import os

load_dotenv()

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='us-east-2'
)

bucket = 'goutham-oubt-test'
files = [
    ('data/hello.txt', 'day1/hello.txt'),
    ('data/sample.json', 'day1/sample.json'),
    ('data/sample.csv', 'day1/sample.csv')
]

print('Uploading Day 1 files to S3\n')
for local_file, s3_key in files:
    try:
        s3.upload_file(local_file, bucket, s3_key)
        print(f'Uploaded: {local_file} to s3://{bucket}/{s3_key}')
    except Exception as e:
        print(f'Failed to upload {local_file}: {e}')

print('\nListing Day 1 files in S3:')
print('='*60)

response = s3.list_objects_v2(Bucket=bucket, Prefix='day1/')
if 'Contents' in response:
    for obj in response['Contents']:
        print(f'{obj["Key"]} ({obj["Size"]} bytes)')
else:
    print('No files found')
    
print('\nDay 1 S3 uploads complete')
