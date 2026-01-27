#!/bin/bash
# Build Lambda deployment package
#
# This script explicitly includes only the directories needed for Lambda deployment:
# - lambda/ (Python handler code)
# - docs/ (framework documentation, excluding _legacy)
#
# Why this approach instead of Terraform's excludes?
# - Explicit is better than implicit: we define what goes IN, not what stays OUT
# - Avoids maintenance burden of updating exclude list as repo grows
# - Makes it immediately clear what the Lambda package contains
# - Prevents accidental inclusion of IDE configs, git metadata, etc.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BUILD_DIR="$SCRIPT_DIR/lambda-build"

echo "Building Lambda package..."

# Clean previous build
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

# Copy Lambda handler code (excluding Python cache)
echo "  Copying lambda/..."
mkdir -p "$BUILD_DIR/lambda"
rsync -a \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  "$PROJECT_ROOT/lambda/" \
  "$BUILD_DIR/lambda/"

# Copy docs (excluding _legacy)
echo "  Copying docs/ (excluding _legacy)..."
mkdir -p "$BUILD_DIR/docs"
rsync -a \
  --exclude='_legacy' \
  "$PROJECT_ROOT/docs/" \
  "$BUILD_DIR/docs/"

echo "Build complete: $BUILD_DIR"
echo "Contents:"
find "$BUILD_DIR" -type f | sort | sed 's|^|  |'
