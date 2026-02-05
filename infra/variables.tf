variable "aws_region" {
  type        = string
  description = "AWS region to deploy into."
  default     = "us-east-1"
}

variable "aws_profile" {
  type        = string
  description = "AWS profile to use for deployment (optional)."
  default     = ""
}

variable "function_name" {
  type        = string
  description = "Name for the Lambda function."
  default     = "collaborators-framework-mcp-server"
}

variable "api_name" {
  type        = string
  description = "Name for the API Gateway HTTP API."
  default     = "collaborators-framework-mcp-server"
}

variable "stage_name" {
  type        = string
  description = "Stage name for the API Gateway stage."
  default     = "prod"
}

variable "custom_domain_name" {
  type        = string
  description = "Custom domain name for the API Gateway (optional)."
  default     = ""
}

variable "acm_certificate_arn" {
  type        = string
  description = "ACM certificate ARN for the custom domain (optional)."
  default     = ""
}

variable "log_retention_days" {
  type        = number
  description = "Number of days to retain API Gateway access logs."
  default     = 7
}

variable "disable_quick_reference" {
  type        = bool
  description = "Disable the quick reference tool/resource in the MCP server."
  default     = false
}
