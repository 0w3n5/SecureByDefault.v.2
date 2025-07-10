variable "alert_email_address" {
  type        = string
  description = "Email to receive GuardDuty alerts"
}

variable "tags" {
  type        = map(string)
  description = "Tags to apply"
}
