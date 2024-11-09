# Dockerfile
FROM python:3.11-slim

# Instalar certificados raíz (ca-certificates)
#RUN apt-get update && apt-get install -y ca-certificates

#COPY ./requirements.txt /code/requirements.txt
COPY ./requirements.txt requirements.txt

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip3 install -r requirements.txt

# Crear un directorio para la aplicación
WORKDIR /app

# Copiar los archivos necesarios
COPY downloadYoutubeToMp3.py /app/

# Crear un directorio donde se guardarán las descargas
RUN mkdir -p /app/mp3

# Comando por defecto
#CMD ["python", "downloadYoutubeToMp3.py"]
