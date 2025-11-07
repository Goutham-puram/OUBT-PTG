# OUBT-PTG: AWS Data Engineering Training - Complete Codebase Context

**Last Updated:** November 7, 2025
**Repository:** Goutham-puram/OUBT-PTG
**Branch:** claude/run-end-to-end-test-011CUt94jeTmmurZFrZU2ubS
**Student:** Gayathri Puram
**Training Duration:** 4 Weeks (20 Days)
**Current Status:** Week 1, Day 3

---

## 1. PROJECT OVERVIEW

This repository contains a hands-on AWS Data Engineering training program focused on building real-world data engineering skills using AWS services. The training uses the NYC Yellow Taxi Trip Data as the primary dataset.

### Training Goals:
- Master AWS Services (S3, Lambda, Glue, RDS, Redshift, Athena)
- Learn Python & PySpark for data processing
- Understand SQL & Data Modeling
- Build ETL Pipelines
- Implement Data Warehousing solutions

### Current Progress:
- ✅ Week 1, Day 1: AWS Fundamentals (Completed)
- 🔄 Week 1, Day 2-3: Python & Boto3 (In Progress)
- ⏳ Week 1, Day 4-5: SQL & Data Modeling (Pending)
- ⏳ Week 2-4: Advanced topics (Pending)

---

## 2. REPOSITORY STRUCTURE

```
OUBT-PTG/
├── .git/                          # Git version control
├── .gitignore                     # Git ignore patterns
├── README.md                      # Project overview and quick reference
├── requirements.txt               # Python dependencies
├── Daily Tracker-B3 (1).xlsx     # Training progress tracking spreadsheet
│
├── data/                          # Sample data directory
│   └── hello.txt                 # Sample text file for S3 uploads
│
├── week1/                         # Week 1 learning materials
│   ├── day1_aws_setup/
│   │   └── day1_notes.md         # Detailed Day 1 learning notes
│   └── week1_learnings.md        # Week 1 summary (empty/WIP)
│
└── Python Scripts (Root Level):
    ├── check_env.py              # Environment variable validator
    ├── debug_env.py              # Credential debugging tool
    ├── test_aws.py               # Comprehensive AWS connectivity test
    ├── test_permissions.py       # IAM permissions validation
    ├── enable_versioning.py      # S3 bucket versioning enabler
    └── day1_upload.py            # Day 1 S3 file upload script
```

---

## 3. FILE DESCRIPTIONS & PURPOSES

### Configuration Files

#### `.gitignore`
**Purpose:** Prevents sensitive and unnecessary files from being committed to Git
**Key Exclusions:**
- AWS credentials (.env, *.pem, *.key, .aws/)
- Python cache (__pycache__/, *.pyc)
- Virtual environments (venv/, env/, .venv/)
- Data files (*.csv, *.parquet, *.json)
- IDE settings (.vscode/, .idea/)
- OS files (.DS_Store, Thumbs.db)
- Logs (*.log)

**Security Note:** Ensures AWS credentials never get committed to version control

#### `requirements.txt`
**Purpose:** Defines Python package dependencies
**Dependencies:**
```
boto3==1.34.144          # AWS SDK for Python
pandas==2.2.2            # Data manipulation library
numpy==1.26.4            # Numerical computing
psycopg2-binary==2.9.9   # PostgreSQL adapter
python-dotenv==1.0.1     # Environment variable loader
```

**Installation:** `pip install -r requirements.txt`

#### `README.md`
**Purpose:** Quick project overview and setup instructions
**Contents:**
- Student information
- Project overview
- Dataset description (NYC Yellow Taxi Trip Data)
- Progress tracker
- Setup commands

---

### Python Scripts (Detailed Breakdown)

#### 1. `check_env.py` (Lines: 21)
**Purpose:** Validates .env file contents and credential format
**Functionality:**
- Loads environment variables from .env file
- Displays AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
- Shows credential lengths (Access: 20 chars, Secret: 40 chars)
- Prints raw .env file contents line-by-line for debugging

**Use Case:** Debugging credential loading issues
**Usage:** `python3 check_env.py`

**Key Operations:**
```python
load_dotenv()                    # Load .env file
os.getenv('AWS_ACCESS_KEY_ID')   # Retrieve credentials
len(access_key)                  # Validate length
```

---

#### 2. `debug_env.py` (Lines: 25)
**Purpose:** Advanced credential debugging with hidden character detection
**Functionality:**
- Loads and displays AWS credentials
- Shows first 10 characters of Access Key
- Shows first 10 and last 5 characters of Secret Key
- Detects whitespace and hidden characters
- Displays Python repr() for exact character inspection

**Use Case:** Identifying hidden characters or encoding issues in credentials
**Usage:** `python3 debug_env.py`

**Special Features:**
- Whitespace detection
- Repr visualization
- Partial key display for security

---

#### 3. `test_aws.py` (Lines: 82)
**Purpose:** Comprehensive AWS connectivity and access test
**Functionality:**
- Tests STS (Security Token Service) connectivity
- Validates IAM user identity
- Lists all accessible S3 buckets
- Checks specific bucket: `goutham-oubt-test`
- Lists up to 5 objects in target bucket

**Use Case:** End-to-end AWS setup validation
**Usage:** `python3 test_aws.py`

**Test Sequence:**
1. Load credentials from .env
2. Create STS client → Get caller identity
3. Create S3 client → List buckets
4. Verify target bucket exists
5. List bucket contents

**Success Output:**
```
✅ AWS Connection Successful!
✅ S3 Access Working!
✅ Found target bucket: goutham-oubt-test
🎉 Day 1 AWS Setup Complete!
```

---

#### 4. `test_permissions.py` (Lines: 58)
**Purpose:** Granular IAM permission testing
**Functionality:**
- **Test 1:** STS GetCallerIdentity (validates basic AWS access)
- **Test 2:** S3 ListBuckets (validates S3 read permissions)
- **Test 3:** S3 bucket-specific access (validates goutham-oubt-test access)

**Use Case:** Diagnosing IAM permission issues
**Usage:** `python3 test_permissions.py`

**Test Structure:**
```
Test 1: STS GetCallerIdentity → Basic Identity
Test 2: S3 ListBuckets → List all buckets
Test 3: Specific Bucket Access → Read goutham-oubt-test
```

**Pass Criteria:** All 3 tests must return "SUCCESS"

---

#### 5. `enable_versioning.py` (Lines: 30)
**Purpose:** Enable S3 bucket versioning for data protection
**Functionality:**
- Connects to S3 using boto3
- Checks current versioning status
- Enables versioning if not already enabled
- Confirms operation success

**Target Bucket:** `goutham-oubt-test`
**Region:** `us-east-2`

**Use Case:** Protecting against accidental file deletions/overwrites
**Usage:** `python3 enable_versioning.py`

**AWS Operations:**
```python
s3.get_bucket_versioning(Bucket=bucket)    # Check status
s3.put_bucket_versioning(                  # Enable versioning
    Bucket=bucket,
    VersioningConfiguration={'Status': 'Enabled'}
)
```

**Output:**
```
Checking versioning status...
Current status: Not Enabled
Enabling versioning...
Versioning enabled successfully
```

---

#### 6. `day1_upload.py` (Lines: 40)
**Purpose:** Upload Day 1 training files to S3
**Functionality:**
- Uploads multiple files from local data/ directory to S3
- Organizes files under day1/ prefix in S3
- Lists uploaded files with sizes
- Reports upload success/failure per file

**Files Uploaded:**
1. `data/hello.txt` → `s3://goutham-oubt-test/day1/hello.txt`
2. `data/sample.json` → `s3://goutham-oubt-test/day1/sample.json`
3. `data/sample.csv` → `s3://goutham-oubt-test/day1/sample.csv`

**Use Case:** Day 1 hands-on S3 upload practice
**Usage:** `python3 day1_upload.py`

**AWS Operations:**
```python
s3.upload_file(local_file, bucket, s3_key)     # Upload
s3.list_objects_v2(Bucket=bucket, Prefix='day1/')  # List
```

**Expected Output:**
```
Uploading Day 1 files to S3

Uploaded: data/hello.txt to s3://goutham-oubt-test/day1/hello.txt
Uploaded: data/sample.json to s3://goutham-oubt-test/day1/sample.json
Uploaded: data/sample.csv to s3://goutham-oubt-test/day1/sample.csv

Listing Day 1 files in S3:
============================================================
day1/hello.txt (50 bytes)
day1/sample.json (116 bytes)
day1/sample.csv (98 bytes)

Day 1 S3 uploads complete
```

---

### Documentation Files

#### `week1/day1_aws_setup/day1_notes.md`
**Purpose:** Detailed Day 1 learning documentation
**Contents:**
- **What I Learned:**
  - AWS Services Overview (S3, Lambda, RDS, Glue, CloudWatch, CloudTrail)
  - IAM Concepts (Users, Groups, Roles, Policies)
  - S3 Features (Versioning, Storage Classes, Bucket Policies, Regions)
- **Hands-On Completed:**
  - AWS account access verification
  - IAM user setup: gayathri.puram
  - S3 bucket verification: goutham-oubt-test
  - File uploads (hello.txt, sample.json, sample.csv)
- **Commands Used:**
  - boto3.client('s3')
  - s3.upload_file()
  - s3.list_objects_v2()
  - s3.put_bucket_versioning()
- **Challenges Faced:**
  1. Credential signature mismatch (missing character in Excel)
  2. IAM permission issues (resolved by adding policies)
- **Key Takeaways:**
  - Credential validation techniques
  - Importance of IAM permissions
  - S3 versioning benefits
  - Secure credential management

#### `week1/week1_learnings.md`
**Status:** Empty/Work in Progress
**Expected Content:** Week 1 consolidated summary

---

## 4. AWS CONFIGURATION

### Required Environment Variables (.env)
```bash
AWS_ACCESS_KEY_ID=<20-character access key>
AWS_SECRET_ACCESS_KEY=<40-character secret key>
AWS_DEFAULT_REGION=us-east-2
```

**⚠️ Security:** .env file is gitignored and must be created locally

### AWS Resources Used
- **S3 Bucket:** goutham-oubt-test
- **Region:** us-east-2 (US East - Ohio)
- **IAM User:** gayathri.puram
- **Permissions Required:**
  - STS: GetCallerIdentity
  - S3: ListBuckets, GetObject, PutObject, GetBucketVersioning, PutBucketVersioning

---

## 5. SETUP INSTRUCTIONS

### Step 1: Clone Repository
```bash
git clone https://github.com/Goutham-puram/OUBT-PTG.git
cd OUBT-PTG
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure AWS Credentials
```bash
# Create .env file
cat > .env << 'EOF'
AWS_ACCESS_KEY_ID=your_20_char_access_key
AWS_SECRET_ACCESS_KEY=your_40_char_secret_key
AWS_DEFAULT_REGION=us-east-2
EOF
```

### Step 4: Validate Setup
```bash
# Test credentials
python3 check_env.py

# Test AWS connectivity
python3 test_aws.py

# Test IAM permissions
python3 test_permissions.py
```

### Step 5: Run Day 1 Tasks
```bash
# Enable S3 versioning
python3 enable_versioning.py

# Upload sample files
python3 day1_upload.py
```

---

## 6. WORKFLOW & DATA FLOW

### Typical Day 1 Workflow
```
1. Credential Setup (.env file)
         ↓
2. Credential Validation (check_env.py / debug_env.py)
         ↓
3. AWS Connectivity Test (test_aws.py)
         ↓
4. Permission Validation (test_permissions.py)
         ↓
5. Enable S3 Features (enable_versioning.py)
         ↓
6. Upload Practice Data (day1_upload.py)
         ↓
7. Verify in AWS Console
```

### Data Flow
```
Local File System (data/)
         ↓
    Python Script
         ↓
    Boto3 SDK
         ↓
    AWS S3 API
         ↓
S3 Bucket (goutham-oubt-test/day1/)
```

---

## 7. KEY CONCEPTS & LEARNING OBJECTIVES

### Day 1: AWS Fundamentals
**Core Skills:**
- AWS account and IAM setup
- S3 bucket creation and management
- Boto3 SDK usage
- Credential management with python-dotenv
- S3 versioning

**AWS Services:**
1. **IAM (Identity and Access Management)**
   - Users, Groups, Roles, Policies
   - Access Key management

2. **S3 (Simple Storage Service)**
   - Bucket operations
   - Object uploads/downloads
   - Versioning
   - Storage classes

3. **STS (Security Token Service)**
   - Identity validation
   - GetCallerIdentity API

**Python Skills:**
- Environment variable management
- boto3 client creation
- Exception handling
- File I/O operations

---

## 8. COMMON ISSUES & SOLUTIONS

### Issue 1: Signature Mismatch Error
**Symptom:** `SignatureDoesNotMatch` error from AWS
**Cause:** Incorrect secret key (missing/extra characters)
**Solution:**
- Validate secret key length = 40 characters
- Use `debug_env.py` to inspect for hidden characters
- Re-copy credentials from AWS Console

### Issue 2: Access Denied Errors
**Symptom:** `AccessDenied` or `UnauthorizedOperation`
**Cause:** Missing IAM permissions
**Solution:**
- Run `test_permissions.py` to identify missing permissions
- Add required policies in AWS IAM Console
- Verify user has attached policies (not just group membership)

### Issue 3: Import Errors
**Symptom:** `ModuleNotFoundError: No module named 'boto3'`
**Cause:** Dependencies not installed
**Solution:** `pip install -r requirements.txt`

### Issue 4: .env File Not Found
**Symptom:** Credentials show as None
**Cause:** .env file missing or in wrong location
**Solution:**
- Ensure .env is in project root directory
- Check .env file permissions
- Use `check_env.py` to debug

---

## 9. TRAINING CURRICULUM (4-Week Plan)

### Week 1: Foundations
- Day 1: AWS Fundamentals & S3 (✅ Completed)
- Day 2-3: Python & Boto3 (🔄 In Progress)
- Day 4-5: SQL & Data Modeling (⏳ Pending)

### Week 2: Data Processing
- Lambda functions
- Glue ETL jobs
- Data transformations

### Week 3: Data Warehousing
- RDS setup
- Redshift architecture
- Data loading strategies

### Week 4: Analytics & Optimization
- Athena queries
- Performance tuning
- Best practices

---

## 10. DATASET INFORMATION

**Dataset:** NYC Yellow Taxi Trip Data
**Source:** NYC Taxi & Limousine Commission
**Format:** CSV/Parquet
**Usage:** Real-world data for ETL pipeline development

**Typical Fields:**
- Pickup/dropoff datetime
- Passenger count
- Trip distance
- Fare amount
- Payment type
- Rate code

---

## 11. TECHNOLOGY STACK

### Cloud Platform
- **AWS** (Amazon Web Services)

### AWS Services
- **S3:** Object storage
- **Lambda:** Serverless compute
- **Glue:** ETL service
- **RDS:** Relational database (PostgreSQL)
- **Redshift:** Data warehouse
- **Athena:** SQL query engine
- **CloudWatch:** Monitoring
- **CloudTrail:** Audit logging

### Programming Languages
- **Python 3.11.14**
- **SQL**

### Python Libraries
- **boto3:** AWS SDK
- **pandas:** Data manipulation
- **numpy:** Numerical computing
- **psycopg2:** PostgreSQL adapter
- **python-dotenv:** Environment management

### Tools
- Git/GitHub
- Excel (Progress tracking)

---

## 12. SECURITY BEST PRACTICES

### Implemented
✅ .env file for credential storage
✅ .gitignore excludes sensitive files
✅ No hardcoded credentials
✅ IAM user with specific permissions (not root)

### Recommended
- Use IAM roles instead of access keys when possible
- Enable MFA on AWS account
- Rotate access keys regularly
- Use AWS Secrets Manager for production
- Implement least privilege principle

---

## 13. NEXT STEPS (Days 2-3)

### Python & Boto3 Deep Dive
- Advanced boto3 operations
- Error handling patterns
- Pagination for large datasets
- Boto3 resource vs client APIs
- Working with S3 object metadata

### Planned Scripts
- Batch file operations
- S3 to local sync
- Recursive directory uploads
- Object lifecycle management

---

## 14. USEFUL COMMANDS REFERENCE

### Git Commands
```bash
git status                          # Check repository status
git add .                          # Stage all changes
git commit -m "message"            # Commit changes
git push -u origin <branch>        # Push to remote branch
```

### Python Commands
```bash
python3 --version                  # Check Python version
pip3 list                         # List installed packages
pip3 install -r requirements.txt  # Install dependencies
python3 script.py                 # Run Python script
```

### AWS CLI (if available)
```bash
aws s3 ls                         # List S3 buckets
aws s3 ls s3://bucket-name/       # List bucket contents
aws iam get-user                  # Get current user info
aws configure                     # Configure AWS CLI
```

---

## 15. REPOSITORY METADATA

**Repository URL:** https://github.com/Goutham-puram/OUBT-PTG
**Current Branch:** claude/run-end-to-end-test-011CUt94jeTmmurZFrZU2ubS
**Main Branch:** (to be determined)
**Total Files:** 13 (excluding .git/)
**Total Python Scripts:** 6
**Total Documentation Files:** 3
**Git Status:** Clean (no uncommitted changes)

**Recent Commits:**
1. 7204d35 - Fix formatting in progress tracker section
2. 0210df6 - test
3. 8fec7da - Fix .gitignore and ignore env files
4. 3030e8c - created skeliton

---

## 16. GLOSSARY

**S3:** Simple Storage Service - AWS object storage
**IAM:** Identity and Access Management - AWS access control
**Boto3:** AWS SDK for Python
**ETL:** Extract, Transform, Load - Data processing pipeline
**STS:** Security Token Service - AWS authentication service
**ARN:** Amazon Resource Name - Unique resource identifier
**Bucket:** S3 container for objects
**Object:** File stored in S3
**Versioning:** S3 feature to track object changes
**Access Key:** Public AWS credential component (20 chars)
**Secret Key:** Private AWS credential component (40 chars)

---

## 17. CONTACT & SUPPORT

**Student:** Gayathri Puram
**GitHub Username:** Goutham-puram
**Repository Issues:** https://github.com/Goutham-puram/OUBT-PTG/issues

---

## 18. CHANGELOG

**November 7, 2025:**
- Created comprehensive codebase context document
- Completed Day 1 AWS fundamentals
- Working on Week 1, Day 3 tasks

---

**End of Codebase Context Document**
**Generated by:** Claude Code Agent
**Purpose:** ChatGPT context reference for OUBT-PTG repository
