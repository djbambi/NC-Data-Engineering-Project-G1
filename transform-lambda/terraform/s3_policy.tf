#DOCUMENT
data "aws_iam_policy_document" "s3_document" {
  statement {
    sid       = "VisualEditor0"
    actions   = ["s3:GetObject"]
    resources = [
      "${aws_s3_bucket.bucket_one.arn}/*",
    ]
  }
   statement {
    actions   = ["s3:PutObject","s3:PutObjectAcl",]
    resources = [
      "${aws_s3_bucket.bucket_two.arn}",
      "${aws_s3_bucket.bucket_two.arn}/*"
      
    ]
  }
   statement {
    actions = ["s3:ListBucket"]

    resources = [
      "${aws_s3_bucket.bucket_one.arn}",
      "${aws_s3_bucket.bucket_two.arn}",
      "${aws_s3_bucket.bucket_three.arn}",
      "${aws_s3_bucket.bucket_one.arn}/*",
      "${aws_s3_bucket.bucket_two.arn}/*",
      "${aws_s3_bucket.bucket_three.arn}/*",
    ]
  }
}

#ATTACH DOC TO POLICY
resource "aws_iam_policy" "s3_policy" {
  name_prefix = "s3-policy-"
  policy = data.aws_iam_policy_document.s3_document.json
}
# ATTACH POLICY TO IAM ROLE
resource "aws_iam_role_policy_attachment" "policy-attach" {
  role       = aws_iam_role.iam_role.name
  policy_arn = aws_iam_policy.s3_policy.arn
}
