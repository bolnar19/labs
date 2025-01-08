# Dockerfile
FROM python:3.10-slim

# Instalar dependencias del sistema (ffmpeg para la conversión a mp3)
RUN apt-get update && apt-get install -y ffmpeg

# Crear un directorio para la aplicación
WORKDIR /app

# Copiar los archivos necesarios
COPY youtube_downloader.py /app/

# Instalar las dependencias de Python
RUN pip install yt-dlp

# Crear un directorio donde se guardarán las descargas
RUN mkdir -p /app/downloads

# Comando por defecto
CMD ["python", "youtube_downloader.py"]
