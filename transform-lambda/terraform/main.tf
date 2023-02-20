# Required providers
provider "aws" {
  access_key = "AKIA433OBQYSL546QCG3"
  secret_key = "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"
  region = "us-east-1"
}
# # CREATE BUCKETS
#BUCKET ONE - INGESTION
resource "aws_s3_bucket" "bucket_one" {
  bucket_prefix = "ingestion-bucket-"
}
output "bucket_one_arn" {
  value = aws_s3_bucket.bucket_one.arn
}
# # PUT MOCK DATA IN INGESTION
resource "aws_s3_bucket_object" "test_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "test.csv"
  source = "../src/test.csv"
}
# #BUCKET TWO - PROCESSED
# resource "aws_s3_bucket" "bucket_two" {
#   bucket_prefix = "processed-bucket-"
# }
# output "bucket_two_arn" {
#   value = aws_s3_bucket.bucket_two.arn
# }
# #BUCKET THREE - LAMBDA
# resource "aws_s3_bucket" "bucket_three" {
#   bucket_prefix = "lambda-bucket-"
# }
# #dan
# output "bucket_three_arn" {
#   value = aws_s3_bucket.bucket_three.arn
# }

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
      aws_s3_bucket.bucket_one.arn
    ]
    principals {
      type        = "AWS"
      identifiers = [aws_iam_role.iam_role.arn]
    }
  }
}
# data "aws_iam_policy_document" "bucket_policy_doc_2" {
#   statement {
#     sid       = "VisualEditor0"
#     effect    = "Allow"
#     actions   = ["s3:*"]
#     resources = [
#       aws_s3_bucket.bucket_two.arn
#     ]
#     principals {
#       type        = "AWS"
#       identifiers = [aws_iam_role.iam_role.arn]
#     }
#   }
# }
# data "aws_iam_policy_document" "bucket_policy_doc_3" {
#   statement {
#     sid       = "VisualEditor0"
#     effect    = "Allow"
#     actions   = ["s3:*"]
#     resources = [
#       aws_s3_bucket.bucket_three.arn
#     ]
#     principals {
#       type        = "AWS"
#       identifiers = [aws_iam_role.iam_role.arn]
#     }
#   }
# }
# # Attaching policy to the iam role
# resource "aws_iam_role_policy_attachment" "policy-attach" {
#   role       = aws_iam_role.iam_role.name
#   policy_arn = aws_iam_policy_document.iam_policy_doc.arn
# }
#BUCKET POLICIES - SPECIFY BUCKET AND DO
resource "aws_s3_bucket_policy" "transform_bucket_policy_one" {
  bucket = "ingestion-bucket-20230220141140182700000002"
  policy = data.aws_iam_policy_document.bucket_policy_doc.json
}
# resource "aws_s3_bucket_policy" "transform_bucket_policy_two" {
#   bucket = "processed-bucket-20230220141140185700000003"
#   policy = data.aws_iam_policy_document.bucket_policy_doc_2.json
# }
# resource "aws_s3_bucket_policy" "transform_bucket_policy_three" {
#   bucket = "lambda-bucket-20230220141140180700000001"
#   policy = data.aws_iam_policy_document.bucket_policy_doc_3.json
# }
# ADD DEPLOYMENT PACKAGE TO S3
# resource "aws_s3_object" "lambda_zip" {
#   bucket = aws_s3_bucket.bucket_three.id
#   key    = "lambda-deployment.zip"
#   source = "../src/lambda-deployment.zip"
# }
# #CREATE LAMBDA  - LAMBDA WILL NEED PERMISSIONS TO WRITE TRANSFORMED DATA TO BUCKET TWO.
# resource "aws_lambda_function" "transformation_lambda" {
#   function_name = "transformation-lambda"
#   s3_bucket = aws_s3_bucket.bucket_three.bucket
#   s3_key = "lambda-deployment.zip"
#   role         = aws_iam_role.iam_role.arn
#   handler      = "lambda-handler.lambda_handler"
#   runtime      = "python3.9"
# }