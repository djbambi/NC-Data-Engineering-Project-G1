# resource "aws_scheduler_schedule" "ingestion_lambda_scheduler" {
#   name = "${var.ingestion_lambda_name}-schedule"

#   flexible_time_window {
#     mode = "OFF"
#   }

#   schedule_expression = "rate(5 minutes)"

#   target {
#     arn      = "arn:aws:scheduler:::aws-sdk:lambda:invoke"
#     role_arn = aws_iam_role.eventbridge_scheduler_role.arn

#   }
# }

# resource "aws_iam_role" "eventbridge_scheduler_role" {
#     name_prefix = "role-scheduler"
#     assume_role_policy = <<EOF
#     {
#         "Version": "2012-10-17",
#         "Statement": [
#             {
#                 "Effect": "Allow",
#                 "Principal": {
#                     "Service": "scheduler.amazonaws.com"
#                 },
#                 "Action": "sts:AssumeRole"
#             }
#         ]
#     }
#     EOF
# }


resource "aws_cloudwatch_event_rule" "ingestion_lambda_scheduler-" {
    name_prefix = "ingestion_lambda_scheduler-"
    description = "Schedule for the ingestion Lambda Function"
    schedule_expression = "rate(5 minutes)"
}

resource "aws_cloudwatch_event_target" "schedule__ingestion_lambda" {
    rule = aws_cloudwatch_event_rule.ingestion_lambda_scheduler-.name
    target_id = "ingestion_lambda"
    arn = aws_lambda_function.ingestion_lambda.arn
}

resource "aws_lambda_permission" "allow_eventbridge_scheduler" {
  action = "lambda:InvokeFunction"
  function_name = "${var.ingestion_lambda_name}"
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.ingestion_lambda_scheduler-.arn
  source_account = data.aws_caller_identity.current.account_id
}