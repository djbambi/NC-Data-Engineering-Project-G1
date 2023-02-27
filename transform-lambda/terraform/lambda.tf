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
   handler      = "lambda_handler.lambda_handler"
   runtime      = "python3.9"
   timeout      = 300 
   source_code_hash = filebase64sha256("../src/lambda-deployment.zip")
   layers = ["arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python39:3"]
 }