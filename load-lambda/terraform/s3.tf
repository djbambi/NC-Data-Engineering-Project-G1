resource "aws_s3_bucket" "code_bucket" {
  bucket_prefix = "sqhells-code-1"
}

resource "aws_s3_bucket" "data_bucket" {
  bucket_prefix = "sqhells-transform-"
}

resource "aws_s3_object" "loader_lambda_code" {
  bucket = aws_s3_bucket.code_bucket.bucket
  key = "s3_file_loader/loader_function.zip"
  source = "${path.module}/loader_function.zip"
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.data_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.s3_file_loader.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3]
}