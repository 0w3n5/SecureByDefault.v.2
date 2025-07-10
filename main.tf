terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}

module "vpc" {
  source     = "./modules/vpc"
  cidr_block = var.vpc_cidr
  tags       = var.tags
}

module "guardduty" {
  source              = "./modules/guardduty"
  alert_email_address = var.alert_email_address
  tags                = var.tags
}
