output "api_endpoint" {
  description = "Base URL for the MCP HTTP endpoint."
  value       = aws_apigatewayv2_api.mcp.api_endpoint
}
