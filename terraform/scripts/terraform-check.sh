#!/bin/bash

set -e

cd ../clouds/aws/environments/dev

echo "Terraform fmt"
terraform fmt -check -recursive

echo "Terraform init"
terraform init -input=false

echo "Terraform validate"
terraform validate

echo "Terraform plan"
terraform plan -input=false

#echo "TFLint"
#tflint --init
#tflint

#echo "Checkov"
#checkov -d ../../ --framework terraform
