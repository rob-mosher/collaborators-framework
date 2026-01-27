# Infrastructure

Terraform configuration for deploying the Collaborators Framework MCP server to AWS Lambda.

## Deployment Workflow

### 1. Build Lambda Package

```bash
cd infra
./build-lambda.sh
```

This creates a clean deployment package in `lambda-build/` containing only:
- `lambda/` - Python handler code (excluding cache files)
- `docs/` - Framework documentation (excluding `_legacy/`)

**Why a build script?** Explicit inclusion is clearer than exclusion lists. The script makes it immediately obvious what goes into the Lambda package and prevents accidental inclusion of repo metadata, IDE configs, etc.

### 2. Deploy with Terraform
Terraform zips `lambda-build/`, not `docs/` or `lambda/` directly, so rebuilding first ensures documentation-only changes are included in the plan.

```bash
./tf-plan.sh     # Rebuild package, then review changes
terraform apply  # Deploy
```

## Configuration

See [terraform.tfvars.example](terraform.tfvars.example) for configuration options.

## Architecture

- **Lambda Function**: Python 3.11 runtime running the MCP server
- **API Gateway**: HTTP API with CORS configured for MCP protocol
  - Access logs sent to CloudWatch Logs (configurable retention period)
  - Detailed CloudWatch metrics enabled
  - Request throttling: 50 requests/second, 100 burst
- **Custom Domain**: Optional custom domain with ACM certificate
- **IAM**: Minimal permissions (CloudWatch Logs only)

## Monitoring

Access logs are available in CloudWatch Logs at `/aws/apigateway/<api-name>`. The logs include:
- Request ID, IP address, and timestamp
- HTTP method, route, and status code
- Response length and integration errors

CloudWatch metrics are automatically published for:
- Request count
- Latency (4xx/5xx errors, integration latency)
- Data transferred
