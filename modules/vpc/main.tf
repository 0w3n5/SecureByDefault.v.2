resource "aws_vpc" "this" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags                 = merge(var.tags, { Name = "secure-vpc" })
}

# No public subnets or NAT gateways — Zero Trust!
