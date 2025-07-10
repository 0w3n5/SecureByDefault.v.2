# SecureByDefault.v.2
Absolutely — here’s a concise and professional `README.md` for your **Secure-by-Default AWS Terraform Project**:

---

```markdown
# Secure-by-Default AWS Terraform Blueprint

A minimal and secure-by-default Terraform project for small teams deploying to AWS. This blueprint follows zero-trust principles and enables continuous threat monitoring using GuardDuty.

## 🔐 Features

- Secure, DNS-enabled VPC (no public subnets or open ports)
- AWS GuardDuty enabled for threat detection
- SNS-based email alerts for GuardDuty findings (no Lambda)
- Follows zero-trust and least privilege best practices
- Modular, reusable Terraform structure

## 📁 Structure

```

secure-by-default-aws/
├── main.tf              # Root module wiring all components
├── variables.tf         # Input variables
├── terraform.tfvars     # Default variable values
├── outputs.tf           # Root outputs
└── modules/
├── vpc/             # Secure VPC
└── guardduty/       # GuardDuty + SNS alerts

````

## 🚀 Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/your-org/secure-by-default-aws.git
   cd secure-by-default-aws
````

2. Customize `terraform.tfvars`:

   ```hcl
   aws_region          = "eu-west-2"
   aws_profile         = "default"
   alert_email_address = "your@email.com"
   ```

3. Deploy:

   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

4. ✅ Confirm the SNS email subscription.

## 🛡️ Security Principles Applied

* **Zero Trust**: No implicit access, no public subnets or open ports
* **Least Privilege**: Minimal IAM roles and services used
* **Continuous Monitoring**: GuardDuty alerts routed to email

## 🧱 Extend With

* S3 module with encryption and public access blocking
* IAM module for least-privilege user creation
* Bastion host in a hardened subnet

---

**Author**: Owen Sweet
```
