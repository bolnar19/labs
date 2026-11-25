module "vpc" {

  source = "../../modules/vpc"

  vpc_name           = var.vpc_name
  vpc_cidr           = var.vpc_cidr
  public_subnet_cidr = var.public_subnet_cidr

}

module "security_group" {

  source = "../../modules/security-group"

  vpc_id = module.vpc.vpc_id

  security_group_name        = var.security_group_name
  security_group_description = var.security_group_description

}

module "ec2" {

  source = "../../modules/ec2"

  ec2_name          = var.ec2_name
  ec2_ami           = var.ec2_ami
  ec2_instance_type = var.ec2_instance_type

  subnet_id = module.vpc.public_subnet_id

  security_group_id = module.security_group.security_group_id

}

module "s3" {

  source = "../../modules/s3"

  bucket_name = var.bucket_name

}
