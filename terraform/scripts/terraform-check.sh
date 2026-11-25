#!/bin/bash

set -e

# Paths
TERRAFORM_ROOT="../clouds"
ENVIRONMENT="${1:-dev}"
AWS_ENV="../clouds/aws/environments/${ENVIRONMENT}"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Functions
run_step() {

    STEP_NAME="$1"
    COMMAND="$2"

    echo
    echo -e "${BLUE}====================================================${NC}"
    echo -e "${YELLOW}[STEP]${NC} $STEP_NAME"
    echo -e "${YELLOW}[CMD ]${NC} $COMMAND"

    START=$(date +%s)
    eval "$COMMAND"
    END=$(date +%s)

    echo -e "${GREEN}[ TIME ]${NC} $STEP_NAME ($((END - START))s)"
}

# Start
cd "$(dirname "$0")"

echo
echo -e "${BLUE}====================================================${NC}"
echo -e "${BLUE}Terraform Validation Pipeline${NC}"
echo "Terraform root : $(realpath $TERRAFORM_ROOT)"
echo "Environment    : $ENVIRONMENT"
echo -e "${BLUE}====================================================${NC}"

# Format
run_step \
  "Terraform Format Check" \
  "terraform fmt -check -recursive -diff ${TERRAFORM_ROOT} || true"

run_step \
  "Terraform Format Applying" \
  "terraform fmt -recursive ${TERRAFORM_ROOT}"

# AWS env
cd "$AWS_ENV"

echo
echo -e "${BLUE}====================================================${NC}"
echo -e "${BLUE}Terraform execution directory:${NC}"
pwd
echo -e "${BLUE}====================================================${NC}"

# Validation
run_step \
  "Terraform Init" \
  "terraform init -input=false"

run_step \
  "Terraform Validate" \
  "terraform validate"

run_step \
  "Terraform Plan" \
  "terraform plan -input=false"

# Summary
echo
echo -e "${GREEN}====================================================${NC}"
echo -e "${GREEN}Validation completed successfully${NC}"
echo -e "${GREEN}====================================================${NC}"
