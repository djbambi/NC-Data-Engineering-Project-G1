
resource "aws_cloudwatch_event_rule" "ingestion_lambda_scheduler-" {
    name_prefix = "ingestion_lambda_scheduler-"
    description = "Schedule for the ingestion Lambda Function"
    schedule_expression = "rate(5 minutes)"
}

resource "aws_cloudwatch_event_target" "schedule__ingestion_lambda" {
    rule = aws_cloudwatch_event_rule.ingestion_lambda_scheduler-.name
    target_id = "ingestion"
    arn = aws_lambda_function.ingestion.arn
}

resource "aws_lambda_permission" "allow_eventbridge_scheduler" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ingestion.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.ingestion_lambda_scheduler-.arn
  source_account = data.aws_caller_identity.current.account_id
}
