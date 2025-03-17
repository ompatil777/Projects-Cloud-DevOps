terraform {
  required_version = "~> 1.1"
  required_providers {
    aws = {
      version = "~>3.1"
    }
  }
}

provider "aws" {
  region     = "ap-south-1"
}

resource "aws_instance" "myEC2" {
  ami = "ami-02972a2a0ac299bb7" #your ami id
  instance_type = "t2.micro"
  count = 2
  tags = {
    Name = "Terraform-EC2 ${count.index+1}"
  }
}