# Cloud Computing Basics

## What is Cloud Computing?

**Cloud computing** provides on-demand access to computing resources over the internet, without owning physical hardware.

```
Traditional (On-Premises):          Cloud:

┌─────────────────────────┐        ┌─────────────────────────┐
│   Your Data Center      │        │   Cloud Provider        │
│                         │        │                         │
│  Buy servers            │        │  Rent by the hour       │
│  Maintain hardware      │        │  No maintenance         │
│  Fixed capacity         │        │  Elastic scaling        │
│  Upfront cost           │        │  Pay-as-you-go          │
│  Full control           │        │  Managed services       │
└─────────────────────────┘        └─────────────────────────┘
```

## Service Models

### IaaS, PaaS, SaaS

```
Cloud Service Stack:

┌─────────────────────────────────────────────────────────────┐
│  SaaS (Software as a Service)                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Gmail, Dropbox, Salesforce, Slack                   │   │
│  │  You manage: Just use it                             │   │
│  │  Provider manages: Everything                        │   │
│  └─────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│  PaaS (Platform as a Service)                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Heroku, Google App Engine, AWS Elastic Beanstalk   │   │
│  │  You manage: Code, data                              │   │
│  │  Provider manages: Runtime, OS, servers              │   │
│  └─────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│  IaaS (Infrastructure as a Service)                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  AWS EC2, Google Compute, Azure VMs                  │   │
│  │  You manage: OS, runtime, code, data                 │   │
│  │  Provider manages: Virtualization, servers, network  │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Major Cloud Providers

| Provider | Strengths | Key Services |
|----------|-----------|--------------|
| **AWS** | Largest, most services | EC2, S3, Lambda |
| **Google Cloud** | ML/AI, data analytics | BigQuery, TPUs |
| **Azure** | Enterprise, Microsoft integration | VMs, Active Directory |

## Core Cloud Services

### Compute

```
Compute Options:

Virtual Machines (IaaS):
  - Full control, any OS
  - AWS EC2, GCP Compute Engine, Azure VMs
  - Pay by hour, various sizes

Containers:
  - Package app + dependencies
  - AWS ECS/EKS, GCP GKE, Azure AKS
  - Kubernetes orchestration

Serverless (Functions):
  - Run code without servers
  - AWS Lambda, GCP Functions, Azure Functions
  - Pay per execution, auto-scales
```

### Storage

```
Storage Types:

Object Storage (files, media):
  - AWS S3, GCP Cloud Storage, Azure Blob
  - Unlimited capacity, pay per GB
  - Access via HTTP/API

Block Storage (VM disks):
  - AWS EBS, GCP Persistent Disk
  - Attached to VMs
  - SSD or HDD options

Database:
  - Managed SQL: AWS RDS, Cloud SQL
  - NoSQL: DynamoDB, Firestore, CosmosDB
  - No maintenance, automatic backups
```

## Python in the Cloud

### AWS with Boto3

```python
import boto3

# S3: Upload/download files
s3 = boto3.client('s3')

# Upload file
s3.upload_file('local_file.csv', 'my-bucket', 'data/file.csv')

# Download file
s3.download_file('my-bucket', 'data/file.csv', 'downloaded.csv')

# List objects
response = s3.list_objects_v2(Bucket='my-bucket', Prefix='data/')
for obj in response.get('Contents', []):
    print(obj['Key'], obj['Size'])
```

### Google Cloud

```python
from google.cloud import storage, bigquery

# Cloud Storage
storage_client = storage.Client()
bucket = storage_client.bucket('my-bucket')

# Upload
blob = bucket.blob('data/file.csv')
blob.upload_from_filename('local_file.csv')

# BigQuery
bq_client = bigquery.Client()
query = """
    SELECT * FROM `project.dataset.table`
    WHERE date > '2024-01-01'
"""
df = bq_client.query(query).to_dataframe()
```

### Azure

```python
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential

# Blob Storage
credential = DefaultAzureCredential()
blob_service = BlobServiceClient(
    account_url="https://myaccount.blob.core.windows.net",
    credential=credential
)

# Upload
container = blob_service.get_container_client("my-container")
with open("local_file.csv", "rb") as data:
    container.upload_blob("data/file.csv", data)
```

## Cloud for Machine Learning

### Managed ML Services

```
ML Platforms:

┌─────────────────────────────────────────────────────────────┐
│                    AWS SageMaker                            │
│  - Managed notebooks                                        │
│  - Built-in algorithms                                      │
│  - Model training and deployment                            │
│  - GPU instances available                                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                 Google Vertex AI                            │
│  - AutoML (no-code ML)                                      │
│  - Custom training                                          │
│  - TPU access                                               │
│  - ML pipelines                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   Azure ML Studio                           │
│  - Drag-and-drop ML                                         │
│  - Automated ML                                             │
│  - Integration with VS Code                                 │
└─────────────────────────────────────────────────────────────┘
```

### GPU Instances

```python
# Example: Launch GPU instance for training

# AWS EC2 GPU instances:
# - p3.2xlarge: 1x V100 (16GB) - ~$3/hour
# - p3.8xlarge: 4x V100 - ~$12/hour
# - p4d.24xlarge: 8x A100 - ~$33/hour

# Google Cloud:
# - a2-highgpu-1g: 1x A100 - ~$3/hour
# - a2-highgpu-8g: 8x A100 - ~$25/hour

# Can also attach GPUs to regular VMs:
# gcloud compute instances create my-gpu-vm \
#     --machine-type=n1-standard-8 \
#     --accelerator=type=nvidia-tesla-v100,count=1
```

## Serverless Computing

### AWS Lambda Example

```python
# lambda_function.py

import json
import boto3

def lambda_handler(event, context):
    """Process uploaded S3 file."""
    
    # Get bucket and key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['key']
    
    # Process file
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    
    # Do something with content
    line_count = len(content.split('\n'))
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'file': key,
            'lines': line_count
        })
    }
```

### When to Use Serverless

```
Good for Serverless:
  ✓ Event-driven processing
  ✓ Variable/unpredictable load
  ✓ Short-running tasks (<15 min)
  ✓ API endpoints
  
Not Good for Serverless:
  ✗ Long-running jobs
  ✗ GPU computation
  ✗ Stateful applications
  ✗ Constant high load (cost)
```

## Cost Management

### Pricing Models

```
Cloud Pricing:

On-Demand:
  - Pay by hour/second
  - Most expensive
  - Maximum flexibility

Reserved (1-3 years):
  - 30-75% cheaper
  - Commitment required
  - Good for steady workloads

Spot/Preemptible:
  - 60-90% cheaper
  - Can be interrupted
  - Good for fault-tolerant batch jobs
```

### Cost Optimization Tips

```python
# 1. Use spot instances for training
# 2. Right-size instances (don't over-provision)
# 3. Auto-scaling for variable loads
# 4. Use serverless for intermittent workloads
# 5. Choose appropriate storage tier

# Example: S3 storage tiers
# Standard:          $0.023/GB/month (frequent access)
# Infrequent Access: $0.0125/GB/month
# Glacier:           $0.004/GB/month (archival)
# Glacier Deep:      $0.00099/GB/month (rarely accessed)
```

## Getting Started

### Local Development → Cloud

```python
# 1. Develop locally
python train.py --data local_data.csv

# 2. Test with cloud storage
python train.py --data s3://bucket/data.csv

# 3. Run on cloud compute
# Deploy to EC2/GCE or use managed service

# 4. Scale up
# Increase instance size or use multiple instances
```

### Basic Cloud Workflow

```
1. Create cloud account
2. Set up credentials/authentication
3. Install SDK (boto3, google-cloud, azure)
4. Store data in cloud storage
5. Launch compute instance or use managed service
6. Run workload
7. Download results / deploy model
8. Shut down resources!
```

## Summary

| Service Type | What It Provides | Example |
|--------------|------------------|---------|
| **IaaS** | Virtual machines | EC2, Compute Engine |
| **PaaS** | Application platform | Heroku, App Engine |
| **SaaS** | Complete applications | Gmail, Dropbox |
| **Storage** | Files and databases | S3, Cloud Storage |
| **Serverless** | Run code on events | Lambda, Functions |
| **ML Platform** | Managed ML training | SageMaker, Vertex AI |

Key takeaways:

- Cloud provides flexible, on-demand computing
- Pay-as-you-go vs large upfront investment
- Choose service level based on control needs
- Use managed services to reduce operational burden
- Monitor costs—easy to overspend
- Spot/preemptible instances for cost savings
- Python SDKs available for all major clouds
