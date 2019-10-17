provider "aws" {
	access_key = "AKIA4TESCCCV7N3WRE4M"
	secret_key = "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"
	region = "ap-south-1"
	}
resource "aws_s3_bucket" "sree" {
	bucket = "sree445"
	}