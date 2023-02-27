resource "aws_lambda_function" "ingestion" {
  function_name = "${var.ingestion_lambda_name}"
  s3_bucket = aws_s3_bucket.code_bucket.bucket
  s3_key = "ingestion/ingestion_function.zip"
  role = aws_iam_role.lambda_role.arn
  handler = "lambda_function.lambda_handler"
  runtime = "python3.9"
  timeout = 300
  #source_code_hash = filebase64sha256("ingestion_function.zip")
  layers = ["arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python39:3"]
}

resource "aws_lambda_function" "transform" {
  function_name = "${var.transform_lambda_name}"
  s3_bucket = aws_s3_bucket.code_bucket.bucket
  s3_key = "transform/transform_function.zip"
  role = aws_iam_role.lambda_role.arn
  handler = "lambda_handler.lambda_handler"
  runtime = "python3.9"
  timeout = 300
  #source_code_hash = filebase64sha256("transform_function.zip")
  layers = ["arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python39:3"]
}
resource "aws_lambda_function" "loader" {
  function_name = "${var.loader_lambda_name}"
  s3_bucket = aws_s3_bucket.code_bucket.bucket
  s3_key = "loader/loader_function.zip"
  role = aws_iam_role.lambda_role.arn
  handler = "warehouse_loader.lambda_handler"
  runtime = "python3.9"
  timeout = 300
  #source_code_hash = filebase64sha256("loader_function.zip")
  layers = ["arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python39:3"]
}

resource "aws_lambda_permission" "allow_s3_one" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.transform.function_name
  principal = "s3.amazonaws.com"
  source_arn = aws_s3_bucket.data_bucket_one.arn
  source_account = data.aws_caller_identity.current.account_id
}
resource "aws_lambda_permission" "allow_s3_two" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.loader.function_name
  principal = "s3.amazonaws.com"
  source_arn = aws_s3_bucket.data_bucket_two.arn
  source_account = data.aws_caller_identity.current.account_id
}

