# Overview

This project involves creating a simple web application writen python with the following features:
- A REST API to interact with an S3 bucket.
- A Dockerized application.
- Automated CI/CD pipeline using GitHub Actions.
- Deployment to AWS ECS using Fargate.

## Create AWS account 

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
# Create Dockerfile 

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]

## Setting Up GitHub Secrets

Make sure to store your AWS credentials in GitHub Secrets:

Go to your repository on GitHub.
Click on `Settings`.
Click on `Secrets and variables` > `Actions`.
Click `New repository secret`.
Add the following secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`


# Create an ECR Repository
Create an Amazon ECR repository to store your images. You can create a repository using following command.

aws ecr create-repository --repository-name my-ecr-repo --region <use region>


# Create ECS Cluster
   Create an ECS cluster
 aws ecs create-cluster --cluster-name ${{ env.ECS_CLUSTER }}

# Task Definition ECS
aws ecs register-task-definition --cli-input-json file://<task-definition.json>

{
	"family": "task-definition",
	"networkMode": "awsvpc",
	"containerDefinitions": [{
		"name": "task-daxap-case",
		"image": "<accountid>.dkr.ecr.us-east-1.amazonaws.com/task-daxap-case:latest",
		"portMappings": [{
			"containerPort": 5000,
			"protocol": "tcp"
		}],
		"essential": true
	}],
	"requiresCompatibilities": [
		"FARGATE"
	],
	"cpu": "256",
	"memory": "512",
	"executionRoleArn": "arn:aws:iam::300886884337:role/ecstaskexecutionrole",
	"taskRoleArn": "arn:aws:iam::300886884337:role/acsaccess3"   
}

# Create Service 
aws ecs create-service --cluster <first-cluster> --service-name <first-service> --task-definition <task-definition> --desired-count 1 --launch-type "FARGATE" --network-configuration "awsvpcConfiguration={subnets=[subnet-077c9758],securityGroups=[sg-e29b36ce],assignPublicIp=ENABLED}"

## Notes

 Ensure that your ECS task definition JSON file is correctly formatted and placed at the specified path.
 Make sure the specified subnets and security groups exist in your AWS account and have the necessary configurations.
 This example assumes the use of AWS Fargate. Adjust the `--launch-type` parameter if you are using EC2 instances for your ECS tasks.
 securityGroups=[sg-e29b36ce] open the inbound security group port 5000


Feel free to modify any part of this `README.md` to better fit your project or additional instructions you might need.

After AWS service is running, you can run the following commands. Do not forget to change the IP address.


### POST request 
curl http://<PublicIp-address>:5000/daxap/list

# PUT Request Response
curl -X POST http://44.193.200.166:5000/daxap/put -H "Content-Type: application/json" -d '{"name": "mevlüt", "value": "konya"}'



# Example Response 

{
  "key": "e1d8fc17-4f98-4d38-8f92-d8a1e0e2a3e9.json"
}


# GET Request
curl http://<PublicIp-address>:5000/daxap/get/< example response" (e1d8fc17-4f98-4d38-8f92-d8a1e0e2a3e9.json) > 






