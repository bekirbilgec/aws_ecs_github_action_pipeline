# DAXAP - DevOps Engineer Case Study

## Overview

This project involves creating a simple web application with the following features:
- A REST API to interact with an S3 bucket.
- A Dockerized application.
- Automated CI/CD pipeline using GitHub Actions.
- Deployment to AWS ECS using Fargate or EC2.

## Prerequisites

- AWS account
- Docker
- GitHub account
- AWS CLI configured with appropriate permissions
- AWS IAM roles and policies for ECS and S3 access

## Steps

### 1. Create an S3 Bucket

1. Go to the AWS Management Console.
2. Open the S3 service.
3. Click "Create bucket".
4. Enter a unique bucket name (e.g., `daxap-bucket`).
5. Select your preferred region.
6. Set appropriate access policies.

### 2. Write the Application

Create a simple Flask application with the required endpoints.

**app.py**:
```python
# (Include the content of app.py here)
