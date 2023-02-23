resource "aws_s3_bucket" "ingestion_bucket" {
bucket_prefix = "ingestion-bucket-"
}

resource "aws_s3_bucket" "code_bucket" {
bucket_prefix = "code-bucket-"
}

resource "aws_s3_object" "ingestion_lambda_code" {
  bucket = aws_s3_bucket.code_bucket.bucket
  key = "ingestion_lambda/ingestion_lambda_function.zip"
  source = "${path.module}/ingestion_lambda_function.zip"
}