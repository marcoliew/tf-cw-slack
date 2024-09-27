locals {
  env         = "staging"
  region      = "ap-southeast-2"
  zone1       = "ap-southeast-2a"
  zone2       = "ap-southeast-2b"
  # azs         = data.aws_availability_zones.available.names
  domain_name = "xeniumsolution.online"
  vpc_id      = "vpc-0684e7cb0d3265618"
}


provider "aws" {
  region = local.region
}

terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.49"
    }   
  }
  
}
