resource "aws_lambda_function" "ingestion_lambda" {
  function_name = "${var.ingestion_lambda_name}"
  s3_bucket = aws_s3_bucket.code_bucket.bucket
  s3_key = "ingestion_lambda/ingestion_lambda_function.zip"
  role = aws_iam_role.ingestion_lambda_role.arn
  handler = "lambda_handler.lambda_handler"
  runtime = "python3.9"
  layers = ["arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python39:3"]
}