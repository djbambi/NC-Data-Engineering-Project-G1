# Project Name: Data Ingestion and Transformation Pipeline

## Overview

This project is a data ingestion and transformation pipeline that ingests data from a Postgres Database, transforms it into a star schema, and loads the resultant data files into a data warehouse. The pipeline is designed to be scalable, fault-tolerant, and easily maintainable.

## Architecture

The data ingestion and transformation pipeline consists of the following components:

__Data Sources:__ A Postgres database called ToteSys.  
__AWS S3 Buckets:__ The ingested data is stored in an S3 bucket in CSV format.The Star Schema files are stored in a second S3 bucket in Parquet format. The code files are stored in a third S3 bucket in zip format.  
__AWS Lambda Functions:__ AWS Lambda functions are used to automate 3 discrete parts of the pipeline. These are an ingestion function, a transformation function and a warehouse loader function.  
__Triggers__: AWS EventBridge and Lambda Triggers are used.  
__Layers__: A Lambda layer is used to provide the Pandas library where needed.  
__IAM Roles and Policies:__ IAM roles and policies are used to control access to AWS resources and services.  
__Data Warehouse:__ A postgres database warehouse.

## Prerequisites

* AWS Account
* Python 3.9 installed
* AWS CLI installed
* PG8000
* Pandas
* Terraform

## Usage

1. Clone the repository.
2. Configure AWS CLI with your AWS account credentials.
3. Ensure that there is a connection to your AWS account (e.g. use 'aws sts get-caller-identity' to confirm a connection)
4. The Python files for each Lambda must be zipped up with any necessary libraries. (Note: Do not include the Pandas library as this is too large. It is configured as a layer in AWS through the Terraform code.)
5. The zip files must be stored in the Terraform directory as: ingestion_function.zip, loader_function.zip and transform_function.zip.
6. Change to the Terraform directory. Run (terraform init --> terraform plan --> terraform apply)

## Credentials

__ToteSys Databse__: The hostname, port, database name, username and password need to be included in the db_connection.py file for the ingestionlambda.
__Warehouse Database__: The Warehouse credentials are stored in the AWS Secrets Manager


Example

To run the pipeline, execute the following command: 

Copy code
python pipeline.py
The pipeline will ingest the data from the specified S3 bucket, transform it into a star schema using the specified AWS Glue job, and load the resultant data files into the specified AWS Redshift database.

## Conclusion

This data ingestion and transformation pipeline is designed to be scalable, fault-tolerant, and easily maintainable. It uses AWS Glue to transform the data into a star schema and AWS Redshift to load the data into a data warehouse. Terraform is used to provision the necessary infrastructure, including IAM roles and policies, S3 buckets, and AWS Lambda functions. With this pipeline, you can easily ingest and transform data