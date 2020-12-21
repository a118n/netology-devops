provider "aws" {
  profile = "default"
  region  = "eu-central-1"
}

terraform {
  backend "s3" {
    bucket         = "netology-terraform"
    key            = "tf-infra/terraform.tfstate"
    region         = "eu-central-1"
    encrypt        = true
    dynamodb_table = "terraform_locks"
  }
}

locals {
  test_instance_type = {
    stage = "t2.micro"
    prod  = "t2.nano"
  }
  test_instance_count = {
    stage = 1
    prod  = 2
  }
  test2_instances = {
    stage = ["0"]
    prod  = ["0", "1"]
  }
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}
data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "test" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = local.test_instance_type[terraform.workspace]
  count         = local.test_instance_count[terraform.workspace]
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_instance" "test2" {
  for_each      = toset(local.test2_instances[terraform.workspace])
  ami           = data.aws_ami.ubuntu.id
  instance_type = local.test_instance_type[terraform.workspace]
}
