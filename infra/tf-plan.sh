#!/usr/bin/env bash
set -euo pipefail

# Always rebuild the Lambda package so docs/ and lambda/ changes are reflected.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

"$SCRIPT_DIR/build-lambda.sh" >/dev/null
terraform -chdir="$SCRIPT_DIR" plan "$@"

