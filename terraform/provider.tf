provider "aws" {
  shared_credentials_files = ["~/.aws/credentials"]
  region = var.aws_region
} 