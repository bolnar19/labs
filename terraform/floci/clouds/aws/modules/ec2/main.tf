resource "aws_instance" "this" {

  ami                     = var.ec2_ami
  instance_type           = var.ec2_instance_type
  #key_name                = var.ec2_key_name
  #private_ip              = "172.31.46.179"

  vpc_security_group_ids = [
    var.security_group_id
  ]

  tags = {
    Name = var.ec2_name
  }
  //user_data = "${file("ec2-init-script.sh")}"
}