# CREATE BUCKETS

#BUCKET ONE - INGESTION
resource "aws_s3_bucket" "bucket_one" {
  bucket = "ingestion-bucket-sqhells"
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

# BUCKET TWO - PROCESSED
 resource "aws_s3_bucket" "bucket_two" {
   bucket = "processed-bucket-sqhells"
 }
 output "bucket_two_arn" {
   value = aws_s3_bucket.bucket_two.arn
 }

#BUCKET THREE - LAMBDA
 resource "aws_s3_bucket" "bucket_three" {
   bucket = "lambda-bucket-sqhells"
 }

 output "bucket_three_arn" {
   value = aws_s3_bucket.bucket_three.arn
 }