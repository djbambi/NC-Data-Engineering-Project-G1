# CREATE BUCKETS

#BUCKET ONE - INGESTION
resource "aws_s3_bucket" "bucket_one" {
  bucket = "ingestion-bucket-hell-6"
}
output "bucket_one_arn" {
  value = aws_s3_bucket.bucket_one.arn
}

# PUT MOCK DATA IN INGESTION
resource "aws_s3_bucket_object" "design_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "design.csv"
  source = "../test_csv_files/design.csv"
}
resource "aws_s3_bucket_object" "payment_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "payment.csv"
  source = "../test_csv_files/payment.csv"
}
resource "aws_s3_bucket_object" "purchase_order_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "purchase_order.csv"
  source = "../test_csv_files/purchase_order.csv"
}
resource "aws_s3_bucket_object" "sales_order_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "sales_order.csv"
  source = "../test_csv_files/sales_order.csv"
}
resource "aws_s3_bucket_object" "transaction_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "transaction.csv"
  source = "../test_csv_files/transaction.csv"
}






# BUCKET TWO - PROCESSED
 resource "aws_s3_bucket" "bucket_two" {
   bucket = "processed-bucket-hell-6"
 }
 output "bucket_two_arn" {
   value = aws_s3_bucket.bucket_two.arn
 }

#BUCKET THREE - LAMBDA
 resource "aws_s3_bucket" "bucket_three" {
   bucket = "lambda-bucket-hell-6"
 }

 output "bucket_three_arn" {
   value = aws_s3_bucket.bucket_three.arn
 }