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

print('Checking versioning status...')
versioning = s3.get_bucket_versioning(Bucket=bucket)
current_status = versioning.get('Status', 'Not Enabled')
print(f'Current status: {current_status}')

if current_status != 'Enabled':
    print('\nEnabling versioning...')
    s3.put_bucket_versioning(
        Bucket=bucket,
        VersioningConfiguration={'Status': 'Enabled'}
    )
    print('Versioning enabled successfully')
else:
    print('Versioning is already enabled')
