import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os

load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_DEFAULT_REGION', 'us-east-2')

print('Testing AWS Connection with New Permissions\n')
print(f'Using Access Key: {access_key}\n')
print('='*60)

# Test 1: STS GetCallerIdentity
print('1. Testing STS GetCallerIdentity...')
try:
    sts = boto3.client('sts', aws_access_key_id=access_key, 
                       aws_secret_access_key=secret_key, region_name=region)
    identity = sts.get_caller_identity()
    print('   SUCCESS')
    print(f'   User ARN: {identity["Arn"]}')
    print(f'   Account: {identity["Account"]}')
except Exception as e:
    print(f'   FAILED: {e}')

# Test 2: S3 ListBuckets
print('\n2. Testing S3 ListBuckets...')
try:
    s3 = boto3.client('s3', aws_access_key_id=access_key, 
                      aws_secret_access_key=secret_key, region_name=region)
    buckets = s3.list_buckets()
    print('   SUCCESS')
    print(f'   Found {len(buckets["Buckets"])} buckets:')
    for bucket in buckets['Buckets']:
        print(f'      - {bucket["Name"]}')
except Exception as e:
    print(f'   FAILED: {e}')

# Test 3: Check specific bucket
print('\n3. Testing Access to goutham-oubt-test...')
try:
    s3 = boto3.client('s3', aws_access_key_id=access_key, 
                      aws_secret_access_key=secret_key, region_name=region)
    result = s3.list_objects_v2(Bucket='goutham-oubt-test', MaxKeys=5)
    print('   SUCCESS')
    if 'Contents' in result:
        print(f'   Objects: {len(result["Contents"])}')
    else:
        print('   Bucket is empty (ready to use)')
except Exception as e:
    print(f'   FAILED: {e}')

print('\n' + '='*60)
print('If all tests passed, you are ready for Day 1')
print('='*60)
