terraform {
  required_version = ">= 1.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  //  backend "s3" {
  //    bucket         = "mycomponents-tfstate"       # S3 bucket storing the state file
  //    key            = "state/terraform.tfstate"    # Path to the state file within the bucket
  //    region         = "us-east-1"                  # Region where the bucket lives
  //    encrypt        = true                         # Enable server-side encryption at rest
  //    dynamodb_table = "mycomponents_tf_lockid"     # DynamoDB table for state locking
  //  }
}

# Configure the AWS Provider
provider "aws" {
  region     = var.aws_region
  access_key = "test"
  secret_key = "test"

  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true

  endpoints {
    dynamodb       = "http://localhost:4566"
    secretsmanager = "http://localhost:4566"
    s3             = "http://localhost:4566"
    sns            = "http://localhost:4566"
    sqs            = "http://localhost:4566"
    ssm            = "http://localhost:4566"
    ec2            = "http://localhost:4566"
  }

  default_tags {
    tags = merge(
      var.common_tags,
      {
        Environment = var.environment
      }
    )
  }
}
