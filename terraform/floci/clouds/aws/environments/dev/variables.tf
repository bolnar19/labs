# Generals
variable "environment" {
  type = string
}

variable "common_tags" {
  type = map(string)
}

variable "aws_region" {
  type = string
}


# VPC
variable "vpc_name" {
  type = string
}

variable "vpc_cidr" {
  type = string
}

variable "public_subnet_cidr" {
  type = string
}


# Security Group
variable "security_group_name" {
  type = string
}

variable "security_group_description" {
  type = string
}


# EC2
variable "ec2_name" {
  type = string
}

variable "ec2_ami" {
  type = string
}

variable "ec2_instance_type" {
  type = string
}
