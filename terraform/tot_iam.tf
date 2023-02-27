resource "aws_iam_role" "lambda_role" {
    name_prefix = "role-${var.gen_lambda_name}"
    assume_role_policy = <<EOF
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "sts:AssumeRole"
                ],
                "Principal": {
                    "Service": [
                        "lambda.amazonaws.com"
                    ]
                }
            }
        ]
    }
    EOF
}

data "aws_iam_policy_document" "s3_document" {
  statement {

    actions = ["s3:GetObject"]

    resources = [
      "${aws_s3_bucket.code_bucket.arn}/*",
      "${aws_s3_bucket.data_bucket_one.arn}/*",
      "${aws_s3_bucket.data_bucket_two.arn}/*",
    ]
  }
  statement {
    actions   = ["s3:PutObject","s3:PutObjectAcl",]
    resources = [

      "${aws_s3_bucket.data_bucket_one.arn}",
      "${aws_s3_bucket.data_bucket_two.arn}",
      "${aws_s3_bucket.data_bucket_one.arn}/*",
      "${aws_s3_bucket.data_bucket_two.arn}/*"
    ]
  }

  statement {

    actions = ["s3:ListBucket"]

    resources = [
      "${aws_s3_bucket.data_bucket_one.arn}",
      "${aws_s3_bucket.data_bucket_one.arn}/*",
      "${aws_s3_bucket.data_bucket_two.arn}",
      "${aws_s3_bucket.data_bucket_two.arn}/*",
      "${aws_s3_bucket.code_bucket.arn}/*",
    ]
  }
  statement {

    actions = ["s3:ListAllMyBuckets"]

    resources = [
      "arn:aws:s3:::*"
    ]
  }

  statement {

    actions = ["secretsmanager:GetSecretValue"]
    resources = ["*"]
  }

}


data "aws_iam_policy_document" "cw_document" {
  statement {

    actions = [ "logs:CreateLogGroup" ]

    resources = [
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:*"
    ]
  }

  statement {

    actions = [ "logs:CreateLogStream", "logs:PutLogEvents" ]

    resources = [
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${var.ingestion_lambda_name}:*",
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${var.transform_lambda_name}:*",
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${var.loader_lambda_name}:*"
    ]
  }
}



resource "aws_iam_policy" "s3_policy" {
    name_prefix = "s3-policy-${var.gen_lambda_name}"
    policy = data.aws_iam_policy_document.s3_document.json
}


resource "aws_iam_policy" "cw_policy" {
    name_prefix = "cw-policy-${var.gen_lambda_name}"
    policy = data.aws_iam_policy_document.cw_document.json
}

resource "aws_iam_role_policy_attachment" "lambda_s3_policy_attachment" {
    role = aws_iam_role.lambda_role.name
    policy_arn = aws_iam_policy.s3_policy.arn
}

resource "aws_iam_role_policy_attachment" "lambda_cw_policy_attachment" {
    role = aws_iam_role.lambda_role.name
    policy_arn = aws_iam_policy.cw_policy.arn
}