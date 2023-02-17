# Required providers
provider "aws" {
  access_key = "AKIAZXDYKPMVX5JBYP64"
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
  bucket = aws_s3_bucket.bucket_one.id
  key    = "test.csv"
  source = "../src/test.csv"
}
#BUCKET TWO - PROCESSED
resource "aws_s3_bucket" "bucket_two" {
  bucket = "hellsangels-processed-bucket"
}
output "bucket_two_arn" {
  value = aws_s3_bucket.bucket_two.arn
}
#BUCKET THREE - LAMBDA
resource "aws_s3_bucket" "bucket_three" {
  bucket = "hellsangels-lambda-bucket"
}
#dan
output "bucket_three_arn" {
  value = aws_s3_bucket.bucket_three.arn
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
    actions   = ["s3:*"]
    resources = [
      aws_s3_bucket.bucket_one.arn,
      aws_s3_bucket.bucket_two.arn
    ]
    principals {
      type        = "AWS"
      identifiers = [aws_iam_role.iam_role.arn]
    }
  }
}
#BUCKET POLICIES - SPECIFY BUCKET AND DO
resource "aws_s3_bucket_policy" "bucket_policy_doc" {
  bucket = "hellsangels-ingestion-bucket"
  policy = data.aws_iam_policy_document.bucket_policy_doc.json
}
# resource "aws_s3_bucket_policy" "transform_bucket_policy_two" {
#   bucket = aws_s3_bucket.bucket_two.id
#   policy = data.aws_iam_policy_document.bucket_policy_doc.json
# }
# resource "aws_s3_bucket_policy" "transform_bucket_policy_three" {
#   bucket = aws_s3_bucket.bucket_three.id
#   policy = data.aws_iam_policy_document.bucket_policy_doc.json
# }
# ADD DEPLOYMENT PACKAGE TO S3
resource "aws_s3_object" "lambda_zip" {
  bucket = aws_s3_bucket.bucket_three.id
  key    = "lambda-deployment.zip"
  source = "../src/lambda-deployment.zip"
}
#CREATE LAMBDA  - LAMBDA WILL NEED PERMISSIONS TO WRITE TRANSFORMED DATA TO BUCKET TWO.
resource "aws_lambda_function" "transformation_lambda" {
  function_name = "transformation-lambda"
  s3_bucket = aws_s3_bucket.bucket_three.bucket
  s3_key = "lambda-deployment.zip"
  role         = aws_iam_role.iam_role.arn
  handler      = "lambda-handler.lambda_handler"
  runtime      = "python3.9"
}