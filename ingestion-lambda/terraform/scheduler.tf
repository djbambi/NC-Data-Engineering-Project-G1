resource "aws_scheduler_schedule" "ingestion_lambda_scheduler" {
  name = "${var.ingestion_lambda_name}-schedule"

  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "rate(5 minutes)"

  target {
    arn      = "arn:aws:scheduler:::aws-sdk:lambda:invoke"
    role_arn = aws_iam_role.eventbridge_scheduler_role.arn

  }
}

resource "aws_iam_role" "eventbridge_scheduler_role" {
    name_prefix = "role-scheduler"
    assume_role_policy = <<EOF
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "scheduler.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }
    EOF
}

resource "aws_lambda_permission" "allow_eventbridge_scheduler" {
  action = "lambda:InvokeFunction"
  function_name = "${var.ingestion_lambda_name}"
  principal = "events.amazonaws.com"
  source_arn = aws_iam_role.eventbridge_scheduler_role.arn
  source_account = data.aws_caller_identity.current.account_id
}