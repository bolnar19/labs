resource "aws_instance" "this" {

  ami                     = var.ec2_ami
  instance_type           = var.ec2_instance_type

  subnet_id = var.subnet_id

  #key_name                = var.ec2_key_name
  #private_ip              = "172.31.46.179"

  vpc_security_group_ids = [
    var.security_group_id
  ]

  tags = {
    Name = var.ec2_name
  }
  //user_data = "${file("ec2-init-script.sh")}"

//provisioner "remote-exec" {
//  inline = [
//      "sudo yum install httpd php git -y",
//      "sudo systemctl restart httpd",
//      "sudo systemctl enable httpd",
//      "sudo yum install -y amazon-efs-utils",
//    ]
//  }
}
