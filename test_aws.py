import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print('Loading credentials from .env file...\n')

# Get credentials from environment
access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_DEFAULT_REGION', 'us-east-2')

print(f'Access Key: {access_key[:10]}...')
print(f'Region: {region}\n')

try:
    # Create boto3 clients with explicit credentials
    sts = boto3.client(
        'sts',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    
    identity = sts.get_caller_identity()
    
    print('✅ AWS Connection Successful!')
    print(f'User ARN: {identity["Arn"]}')
    print(f'Account: {identity["Account"]}')
    print(f'User ID: {identity["UserId"]}')
    
    # Test S3 access
    print('\n' + '='*50)
    print('Testing S3 Access...')
    print('='*50)
    
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    
    response = s3.list_buckets()
    
    print('✅ S3 Access Working!')
    print(f'\nYour S3 Buckets ({len(response["Buckets"])} total):')
    for bucket in response['Buckets']:
        print(f'  📦 {bucket["Name"]}')
        
    # Check for our specific bucket
    bucket_name = 'goutham-oubt-test'
    if any(b['Name'] == bucket_name for b in response['Buckets']):
        print(f'\n✅ Found target bucket: {bucket_name}')
        
        # List contents
        try:
            result = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=10)
            if 'Contents' in result:
                print(f'   📄 Objects in bucket: {len(result["Contents"])}')
                for obj in result['Contents'][:5]:
                    print(f'      - {obj["Key"]} ({obj["Size"]} bytes)')
            else:
                print('   📭 Bucket is empty')
        except Exception as e:
            print(f'   ⚠️  Could not list objects: {e}')
    else:
        print(f'\n⚠️  Bucket "{bucket_name}" not found')
        
    print('\n' + '='*50)
    print('🎉 Day 1 AWS Setup Complete!')
    print('='*50)
        
except Exception as e:
    print(f'❌ Error: {e}')
    print('\nDebugging info:')
    print(f'  - .env file location: {os.path.abspath(".env")}')
    print(f'  - Access key loaded: {access_key is not None}')
    print(f'  - Secret key loaded: {secret_key is not None}')
