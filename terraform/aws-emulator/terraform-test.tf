terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"

  #access_key = "test"
  #secret_key = "test"

  skip_credentials_validation = true
  skip_requesting_account_id  = true

  endpoints {
    s3     = "https://localhost:9297"
    ec2    = "https://localhost:9297"
    iam    = "https://localhost:9297"
    lambda = "https://localhost:9297"
  }
  s3_use_path_style = true
}

resource "aws_s3_bucket" "demo" {
  bucket = "test-bucket-terraform"
}
