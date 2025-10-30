# Day 1: AWS Fundamentals & Core Skills

Date: October 27, 2025

## What I Learned

### AWS Services Overview
- S3: Object storage for data lakes and file storage
- Lambda: Serverless compute for event-driven processing
- RDS: Managed relational databases (PostgreSQL, MySQL)
- Glue: ETL service for data transformation
- CloudWatch: Monitoring and logging service
- CloudTrail: Audit logging for AWS API calls

### IAM Concepts
- Users: Individual identities with credentials
- Groups: Collections of users with shared permissions
- Roles: Assumable permissions for services
- Policies: JSON documents defining permissions

### S3 Features
- Versioning: Track changes to objects over time
- Storage classes: Standard, Infrequent Access, Glacier
- Bucket policies: Control access to buckets and objects
- Regions: Geographic locations for data storage

## Hands-On Completed

- AWS account access verified
- IAM user credentials configured: gayathri.puram
- S3 bucket verified: goutham-oubt-test
- Bucket versioning enabled
- Uploaded files to S3:
  - hello.txt (50 bytes)
  - sample.json (116 bytes)
  - sample.csv (98 bytes)
- GitHub repository: OUBT-PTG

## Commands Used

Python with Boto3:
- boto3.client('s3') - Create S3 client
- s3.upload_file() - Upload files to S3
- s3.list_objects_v2() - List bucket contents
- s3.put_bucket_versioning() - Enable versioning

## Challenges Faced

1. AWS credential signature mismatch errors
   - Cause: Copied secret key from Excel was missing a character
   - Solution: Carefully re-copied credentials ensuring all 40 characters

2. IAM permissions
   - Initially user had no permissions attached
   - Added necessary S3 and IAM policies

## Key Takeaways

- Always verify credential length (Access Key: 20 chars, Secret Key: 40 chars)
- IAM permissions are critical for AWS access
- S3 versioning protects against accidental deletions
- Environment variables (.env) keep credentials secure
- Never commit credentials to Git
