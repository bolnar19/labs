# Terraform

## Archivos principales de Terraform
Un proyecto de Terraform suele estar compuesto por varios archivos `.tf`, cada uno con una función específica:

* **main.tf:** Definición de los recursos que Terraform creará o administrará en la plataforma destino (AWS, Azure, GCP, Kubernetes, etc.).
* **variables.tf:** Define las variables que se utilizarán en el proyecto para parametrizar los recursos.
* **provider.tf:** Contiene la configuración de Terraform y de los proveedores que se utilizarán.
* **outputs.tf:** Define los valores que Terraform mostrará al finalizar una ejecución exitosa de `terraform apply`.
* ***.tfvars:** Almacena los valores de las variables para cada entorno.

## Links 
* https://github.com/terraform-aws-modules


## Terraform comands

```bash
# Formatea automáticamente el código Terraform según el estándar oficial de HashiCorp.
terraform fmt
terraform fmt -recursive

# Inicia el proyecto
terraform init

# Valida el proyecto
terraform validate

# Muestra lo que ejecutaria en el apply
terraform plan

# Ejecuta el plan, es decir la creación/modificación/eliminación de recursos
terraform apply

# Destruye los recuros
terraform destroy

# Actualiza el lock file .terraform.lock.hcl
terraform init -upgrade

```

## Limpieza

```bash
# Limpieza archivos terraform
rm -rf .terraform* terraform.tfstate terraform.tfstate.backup

```
