module "security_group" {

  source = "../../modules/security-group"

  security_group_name        = var.security_group_name
  security_group_description = var.security_group_description

}

module "ec2" {

  source = "../../modules/ec2"

  ec2_name          = var.ec2_name
  ec2_ami           = var.ec2_ami
  ec2_instance_type = var.ec2_instance_type

  security_group_id = module.security_group.security_group_id

}
