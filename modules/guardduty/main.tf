resource "aws_guardduty_detector" "this" {
  enable = true
}

resource "aws_sns_topic" "gd_alerts" {
  name = "guardduty-alerts"
}

resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.gd_alerts.arn
  protocol  = "email"
  endpoint  = var.alert_email_address
}

resource "aws_cloudwatch_event_rule" "gd_finding_rule" {
  name        = "guardduty-findings"
  description = "Trigger on GuardDuty findings"
  event_pattern = jsonencode({
    source = ["aws.guardduty"],
    "detail-type" = ["GuardDuty Finding"]
  })
}

resource "aws_cloudwatch_event_target" "gd_to_sns" {
  rule = aws_cloudwatch_event_rule.gd_finding_rule.name
  arn  = aws_sns_topic.gd_alerts.arn
}
