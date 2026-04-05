FROM ubuntu:20.04

# Instalar dependencias y act
RUN apt-get update && apt-get install -y sudo curl jq git docker.io && \
    curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | bash

# Establecer el directorio de trabajo
WORKDIR /workspace

# Copiar el contenido del repositorio en el contenedor
#COPY . .

# Ejecutar act al iniciar el contenedor
CMD ["act"]
