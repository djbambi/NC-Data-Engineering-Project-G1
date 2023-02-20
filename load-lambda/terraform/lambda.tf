resource "aws_lambda_function" "s3_file_loader" {
  function_name = "${var.lambda_name}"
  s3_bucket = aws_s3_bucket.code_bucket.bucket
  s3_key = "s3_file_loader/loader_function.zip"
  role = aws_iam_role.lambda_role.arn
  handler = "warehouse_loader.lambda_handler"
  runtime = "python3.9"
  #filename = "function.zip"
  #source_code_hash = filebase64sha256("loader_function.zip")
}

resource "aws_lambda_permission" "allow_s3" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.s3_file_loader.function_name
  principal = "s3.amazonaws.com"
  source_arn = aws_s3_bucket.data_bucket.arn
  source_account = data.aws_caller_identity.current.account_id
}