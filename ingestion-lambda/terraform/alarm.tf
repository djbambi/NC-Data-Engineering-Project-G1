resource "aws_cloudwatch_log_metric_filter" "ingestion_lambda_error" {
    name = "error-filter"
    pattern = "Error"
    log_group_name = "/aws/lambda/${var.ingestion_lambda_name}"

    metric_transformation {
      name = "errors"
      namespace = "ingestion_lambda"
      value = "1"
    }
}

resource "aws_cloudwatch_metric_alarm" "alert_errors" {
    alarm_name = "ingestion-lambda-error"
    comparison_operator = "GreaterThanOrEqualToThreshold"
    evaluation_periods = "1"
    metric_name = "errors"
    namespace = "ingestion-lambda"
    period = "60"
    statistic = "Sum"
    threshold = "1"
    alarm_description = "Error detected in Ingestion Lambda."
    insufficient_data_actions = []
    alarm_actions = [ aws_sns_topic.error_notifications_topic.arn ]
}

resource "aws_sns_topic" "error_notifications_topic" {
  name = "error_notifications_topic"
}

resource "aws_sns_topic_subscription" "error_notifications_email" {
  topic_arn = aws_sns_topic.error_notifications_topic.arn
  protocol  = "email"
  endpoint  = "${var.notifications_email}"
}