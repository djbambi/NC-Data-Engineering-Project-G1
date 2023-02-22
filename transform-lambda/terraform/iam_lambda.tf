# POLICY DOC FOR IAM ROLE
data "aws_iam_policy_document" "iam_policy_doc" {
  statement {
    effect = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

# IAM ROLE
resource "aws_iam_role" "iam_role" {
  name = "transform-iam-role"
  assume_role_policy = data.aws_iam_policy_document.iam_policy_doc.json
}
