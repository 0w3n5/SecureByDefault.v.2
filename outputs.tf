output "vpc_id" {
  description = "The ID of the created VPC"
  value       = module.vpc.vpc_id
}

output "guardduty_sns_topic_arn" {
  description = "SNS Topic ARN for GuardDuty alerts"
  value       = module.guardduty.sns_topic_arn
}
