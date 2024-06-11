# DAXAP - DevOps Engineer Case Study

## Overview

This project involves creating a simple web application with the following features:
- A REST API to interact with an S3 bucket.
- A Dockerized application.
- Automated CI/CD pipeline using GitHub Actions.
- Deployment to AWS ECS using Fargate.

## Steps

### 1. Create AWS account 

# AWS Account Setup and Management

This document provides a guide for setting up and managing your AWS account.

## Creating an AWS Account

**Open AWS Website**:
   Go to [AWS Website](https://aws.amazon.com).

**Click on 'Create an AWS Account'**:
   You will find this button on the top right corner of the homepage.

**Enter Account Information**:
   - **Email address**: Enter your email address.
   - **Password**: Create a strong password.
   - **AWS account name**: Choose a unique account name.

**Contact Information**:
   - **Full Name**: Enter your full name.
   - **Phone number**: Enter a valid phone number.
   - **Country/Region**: Select your country or region.
   - **Address**: Provide your address.

**Payment Information**:
   Enter your credit/debit card details. AWS needs this information to verify your identity and for billing purposes.

**Identity Verification**:
   - **Phone Verification**: AWS will send a verification code to your phone.
   - **Enter the Code**: Enter the code you received.

**Choose Support Plan**:
   Select a support plan that suits your needs. You can choose the free basic plan to start with.

**Complete Sign-Up**:
   Once you complete the steps, AWS will send a confirmation email. Follow the instructions in the email to verify your account.

## Account Setup

After creating your account, follow these steps for initial setup:

**Enable Multi-Factor Authentication (MFA)**:
   - Go to the IAM Dashboard.
   - Select "Manage MFA".
   - Follow the instructions to set up MFA.

**Create IAM Users and Groups**:
   - Create separate IAM users for each individual.
   - Assign users to groups based on their roles.
   - Attach appropriate policies to each group.

**Set Up Billing Alerts**:
   - Go to the AWS Billing Dashboard.
   - Create billing alerts to monitor your AWS usage and costs.

## Security Best Practices

- **Enable MFA** for all IAM users.
- **Use IAM Roles** for applications that need AWS access.
- **Regularly Rotate IAM Keys** to minimize security risks.
- **Monitor AWS Account Activity** using AWS CloudTrail.

## Conclusion

This document provides an overview of setting up and managing your AWS account. For detailed instructions and best practices, refer to the [AWS Documentation](https://docs.aws.amazon.com/).


# AWS S3 Bucket Setup and Access Configuration

This document provides a guide for creating an AWS S3 bucket and configuring it with an access policy that allows "GET", "LIST", and "POST" operations.

## Creating an S3 Bucket

**Sign in to AWS Management Console**:
   Go to the [AWS Management Console](https://aws.amazon.com/console/) and sign in with your credentials.

**Open the S3 Service**:
   In the AWS Management Console, search for "S3" in the search bar and select the S3 service.

**Create a New Bucket**:
   - Click on "Create bucket".
   - Enter a unique bucket name.
   - Select the AWS region where you want to create the bucket.
   - Configure any additional settings as needed (e.g., versioning, tags).
   - Click "Create bucket" at the bottom of the page.

## Configuring Bucket Policy

**Select the Bucket**:
   - Go to the "Buckets" list and select the bucket you created.

**Open the Permissions Tab**:
   - Select the "Permissions" tab.

**Edit the Bucket Policy**:
   - Scroll down to the "Bucket policy" section and click "Edit".
   - Copy and paste the following bucket policy JSON, replacing `your-bucket-name` with the name of your bucket and `your-account-id` with your AWS account ID.

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": "*",
               "Action": [
                   "s3:GetObject",
                   "s3:ListBucket",
                   "s3:PutObject"
               ],
               "Resource": [
                   "arn:aws:s3:::your-bucket-name/*",
                   "arn:aws:s3:::your-bucket-name"
               ]
           }
       ]
   }










###  

### POST request 
curl http://127.0.0.1:5000/daxap/list

# PUT Request Response
curl -X POST http://http://44.198.162.51:5000/daxap/put -H "Content-Type: application/json" -d '{"name": "deneme", "value": "basarili"}'



# Example Response 

{
  "key": "e1d8fc17-4f98-4d38-8f92-d8a1e0e2a3e9.json"
}


# GET Request
curl http://127.0.0.1:5000/daxap/get/< example response" (e1d8fc17-4f98-4d38-8f92-d8a1e0e2a3e9.json) > 