# CREATE BUCKETS

#BUCKET ONE - INGESTION
resource "aws_s3_bucket" "bucket_one" {
  bucket = "ingestion-bucket-hell-900"
}
output "bucket_one_arn" {
  value = aws_s3_bucket.bucket_one.arn
}

# PUT MOCK DATA IN INGESTION
resource "aws_s3_bucket_object" "design_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "design.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/design.csv"
}
resource "aws_s3_bucket_object" "payment_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "payment.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/payment.csv"
}
resource "aws_s3_bucket_object" "purchase_order_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "purchase_order.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/purchase_order.csv"
}

resource "aws_s3_bucket_object" "transaction_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "transaction.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/transaction.csv"
}
resource "aws_s3_bucket_object" "address_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "address.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/address.csv"
}
resource "aws_s3_bucket_object" "counterparty_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "counterparty.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/counterparty.csv"
}
resource "aws_s3_bucket_object" "currency_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "currency.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/currency.csv"
}
resource "aws_s3_bucket_object" "department_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "department.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/department.csv"
}
resource "aws_s3_bucket_object" "payment_type_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "payment_type.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/payment_type.csv"
}
resource "aws_s3_bucket_object" "sales_order_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "sales_order.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/sales_order.csv"
}
resource "aws_s3_bucket_object" "staff_csv" {
  bucket = aws_s3_bucket.bucket_one.id
  key    = "staff.csv"
  source = "../mock_ingestion_bucket_11_files/csv_files/staff.csv"
}







# BUCKET TWO - PROCESSED
 resource "aws_s3_bucket" "bucket_two" {
   bucket = "processed-bucket-hell-900"
 }
 output "bucket_two_arn" {
   value = aws_s3_bucket.bucket_two.arn
 }

#BUCKET THREE - LAMBDA
 resource "aws_s3_bucket" "bucket_three" {
   bucket = "lambda-bucket-hell-900"
 }

 output "bucket_three_arn" {
   value = aws_s3_bucket.bucket_three.arn
 }