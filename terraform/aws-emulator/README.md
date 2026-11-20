# AWS-Emulator

## Sources: 
* https://docs.aws.amazon.com/emulator/latest/userguide/getting-started-docker.html
* https://github.com/aws/aws-emulator

## docker comands

```bash
# build image
docker build -t aws-emulator .

# start
docker compose up -d

# logs
docker compose logs -f
```

## aws-emulator comands

```bash
# version
docker exec -it aws-emulator bash
aws-emulator -v

# health route
curl -k https://127.0.0.1:9297/__admin/health -i

# health route with cert
curl --cacert data/9297/ca.pem https://127.0.0.1:9297/__admin/health
curl --cacert ~/.aws/emulator/9297/ca.pem https://127.0.0.1:9297/__admin/health
```

## aws commands

```bash

# Configure AWS CLI to trust it
export AWS_CA_BUNDLE=data/9297/ca.pem
export AWS_DEFAULT_REGION=us-east-1
export AWS_ENDPOINT_URL=https://127.0.0.1:9297

export AWS_SHARED_CREDENTIALS_FILE=data/9297/emulator_credentials
#export AWS_ACCESS_KEY_ID=test
#export AWS_SECRET_ACCESS_KEY=test

# clear credentials
#unset AWS_ACCESS_KEY_ID
#unset AWS_SECRET_ACCESS_KEY
#unset AWS_SESSION_TOKEN

# AWS CLI call
aws ecs list-clusters
aws sts get-caller-identity
aws s3 ls
aws ec2 describe-vpcs

# aws cli create butket
aws s3api create-bucket --bucket test-bucket-aws-cli --debug

```

## aws cli test, terraform

Create file **terraform-test.tf** and execute terraform create:

```bash
terraform init
terraform plan
terraform apply
```
