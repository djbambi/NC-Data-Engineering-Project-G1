# Required providers
provider "aws" {
  access_key = "AKIAT3ACVIU54E3ZRIAI"
  secret_key = "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"
  region = "us-east-1"
}

# CREATE BUCKETS

#BUCKET ONE - INGESTION
resource "aws_s3_bucket" "bucket_one" {
  bucket = "hellsangels-ingestion-bucket"
}

output "bucket_one_arn" {
  value = aws_s3_bucket.bucket_one.arn
}

# PUT MOCK DATA IN INGESTION
resource "aws_s3_bucket_object" "test_csv" {
  bucket = aws_s3_bucket.bucket_one_bucket.id
  key    = "test.csv"
  source = "../src/test.csv"
}

#BUCKET TWO - PROCESSED
resource "aws_s3_bucket" "bucket_two" {
  bucket = "hellsangels-processed-bucket"
}

output "bucket_two_arn" {
  value = aws_s3_bucket.bucket_one.arn
}

#BUCKET THREE - LAMBDA
resource "aws_s3_bucket" "bucket_three" {
  bucket = "hellsangels-lambda-bucket"
}

output "bucket_two_arn" {
  value = aws_s3_bucket.bucket_one.arn
}



#ROLES AND POLICY

# POLICY DOC FOR IAM ROLE
data "aws_iam_policy_document" "iam_policy_doc" {
  statement {
    effect = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

# IAM ROLE
resource "aws_iam_role" "iam_role" {
  name = "transform-iam-role"
  assume_role_policy = data.aws_iam_policy_document.iam_policy_doc.json
}


#BUCKET POLICY DOC - SPECIFY BUCKET AND THE IAM ROLE
data "aws_iam_policy_document" "bucket_policy_doc" {
  statement {
    sid       = "VisualEditor0"
    effect    = "Allow"
    actions   = ["s3:GetObject", "s3:PutObject"]
    resources = [
      aws_s3_bucket.bucket_one.arn,
      aws_s3_bucket.bucket_two.arn,
      aws_s3_bucket.bucket_three.arn
    ]
    principals {
      type        = "AWS"
      identifiers = [aws_iam_role.iam_role.arn]
    }
  }
}

#BUCKET POLICIES - SPECIFY BUCKET AND DO
resource "aws_s3_bucket_policy" "bucket_policy_one" {
  bucket = aws_s3_bucket.bucket_one.id
  policy = data.aws_iam_policy_document.bucket_policy_doc.json
}

resource "aws_s3_bucket_policy" "bucket_policy_two" {
  bucket = aws_s3_bucket.bucket_one.id
  policy = data.aws_iam_policy_document.bucket_policy_doc.json
}

resource "aws_s3_bucket_policy" "bucket_policy_three" {
  bucket = aws_s3_bucket.bucket_one.id
  policy = data.aws_iam_policy_document.bucket_policy_doc.json
}


#CREATE LAMBDA DEPLOYMENT PACKAGE - LAMBDA WILL NEED PERMISSIONS TO WRITE TRANSFORMED DATA TO BUCKET TWO.
resource "aws_lambda_function" "transformation_lambda" {
  function_name = "transformation-lambda"
  role         = aws_iam_role.iam_role.arn
  handler      = "lambda-handler.lambda_handler"
  runtime      = "python3.9"
  filename     = "lambda-deployment.zip"

  source_code_hash = filebase64sha256("../lambda-deployment.zip")
}

# ADD DEPLOYMENT PACKAGE TO S3 
resource "aws_s3_object" "lambda_zip" {
  bucket = aws_s3_bucket.bucket_three.id
  key    = "lambda-deployment.zip"
  source = "lambda-deployment.zip"
}
