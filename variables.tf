variable "aws_region" {
  type        = string
  description = "AWS region to deploy to"
}

variable "aws_profile" {
  type        = string
  description = "AWS CLI profile to use"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR block for VPC"
  default     = "10.0.0.0/16"
}

variable "alert_email_address" {
  type        = string
  description = "Email for GuardDuty alerts"
}

variable "tags" {
  type        = map(string)
  description = "Common tags"
  default     = {}
}
