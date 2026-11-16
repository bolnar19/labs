# Floci con Terraform

Laboratorio para aprovisionamiento de recursos utilizando **Floci** y **Terraform**, simulando servicios cloud localmente.

## Descargas de Floci
- Floci AWS: https://github.com/floci-io/floci/releases
- Floci Azure: https://github.com/floci-io/floci-az/releases
- Floci GCP: https://github.com/floci-io/floci-gcp/releases
- Floci OCI: https://github.com/floci-io/floci-oci/releases
- Floci UI: https://github.com/floci-io/floci-ui/releases

---

## Configuración del certificado

Para que Terraform confíe en el certificado autofirmado utilizado por Floci Azure, copie el certificado al almacén de confianza del sistema:

```bash
cp data/tls/floci-az-selfsigned-ca.crt /etc/pki/ca-trust/source/anchors/
update-ca-trust
```

# Iniciar servicios con docker-compose

## Iniciar con docker-compose:

```bash
# Start
docker compose up -d

# Stop
docker compose down

# Status
docker ps -a

# Logs
docker compose logs -f
```

## UI Web
- floci-ui: http://localhost:4500  


---

# Referencias

## Video
- Kevo Rojas - *Azure gratis en tu computadora: probé Floci con Terraform*
  - https://youtu.be/W1Nyz5SuKgM

## Repositorio de ejemplo
- https://github.com/kevorojas/floci-azure-terraform
