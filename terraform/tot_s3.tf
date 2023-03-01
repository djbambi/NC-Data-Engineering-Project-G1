resource "aws_s3_bucket" "code_bucket" {
  bucket_prefix = "sqhells-code-1"
}

resource "aws_s3_bucket" "data_bucket_one" {
  bucket_prefix = "sqhells-ingestion-"
}
resource "aws_s3_bucket" "data_bucket_two" {
  bucket_prefix = "sqhells-processed-"
}

resource "aws_s3_object" "ingestion_lambda_code" {
  bucket = aws_s3_bucket.code_bucket.bucket
  key = "ingestion/ingestion_function.zip"
  source = "${path.module}/ingestion_function.zip"
}

resource "aws_s3_object" "transform_lambda_code" {
  bucket = aws_s3_bucket.code_bucket.bucket
  key = "transform/transform_function.zip"
  source = "${path.module}/transform_function.zip"
}

resource "aws_s3_object" "loader_lambda_code" {
  bucket = aws_s3_bucket.code_bucket.bucket
  key = "loader/loader_function.zip"
  source = "${path.module}/loader_function.zip"
}

resource "aws_s3_bucket_notification" "bucket_one_notification" {
  bucket = aws_s3_bucket.data_bucket_one.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.transform.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3_one]
}

resource "aws_s3_bucket_notification" "bucket_two_notification" {
  bucket = aws_s3_bucket.data_bucket_two.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.loader.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3_two]
}