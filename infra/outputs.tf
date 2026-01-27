output "api_endpoint" {
  description = "Base URL for the MCP HTTP endpoint."
  value       = aws_apigatewayv2_api.mcp.api_endpoint
}

output "custom_domain_name" {
  description = "Custom domain name for the MCP endpoint, if configured."
  value       = var.custom_domain_name != "" ? var.custom_domain_name : null
}

output "custom_domain_target" {
  description = "Target domain for the custom domain CNAME, if configured."
  value = try(
    aws_apigatewayv2_domain_name.mcp[0].domain_name_configuration[0].target_domain_name,
    null
  )
}

output "custom_domain_zone_id" {
  description = "Route 53 zone ID for the custom domain, if configured."
  value = try(
    aws_apigatewayv2_domain_name.mcp[0].domain_name_configuration[0].hosted_zone_id,
    null
  )
}

output "cloudwatch_log_group" {
  description = "CloudWatch log group name for API Gateway access logs."
  value       = aws_cloudwatch_log_group.apigw.name
}

output "lambda_function_name" {
  description = "Name of the Lambda function."
  value       = aws_lambda_function.mcp.function_name
}
