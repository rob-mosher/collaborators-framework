variable "aws_region" {
  type        = string
  description = "AWS region to deploy into."
  default     = "us-east-1"
}

variable "function_name" {
  type        = string
  description = "Name for the Lambda function."
  default     = "mcp-hello-world"
}

variable "api_name" {
  type        = string
  description = "Name for the API Gateway HTTP API."
  default     = "mcp-hello-world"
}
