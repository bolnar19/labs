# Dev Environment
environment = "dev"
aws_region  = "us-east-1"

# VPC conf
# vpc_cidr    = "10.0.0.0/16"

# EC2
ec2_name          = "ec2-test"
ec2_ami           = "ami-12345678"
ec2_instance_type = "t3.micro"
#ec2_instance_count  = 2

# Security groups
security_group_name        = "ec2-security-group"
security_group_description = "Security Group EC2"

# Database conf

# Tags
common_tags = {
  ManagedBy   = "Terraform"
  Project     = "Infrastructure"
  Environment = "dev"
  ConstCenter = "engineering"
}
