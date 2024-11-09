# -*- coding: utf-8 -*-

import pytube
#import logging
import mutagen
import time
#import os
import shlex

from mutagen.easyid3 import EasyID3

# Obtener el URL de la lista de reproducción
playlist_url = "https://www.youtube.com/playlist?list=PLV0-i_rHNhfayEhTnncgEVAASKaxO8KuZ"

# Crear un objeto de playlist
playlist = pytube.Playlist(playlist_url)

# Obtener una lista de los videos de la playlist
videos = playlist.videos

# Obtener el índice del video a partir del que se desea comenzar la descarga
start_index = 915

# Inicializar el registrador
#logging.basicConfig(level=logging.INFO)

# Iterar sobre los videos
for index, video in enumerate(videos):
    if index >= start_index:
                
        # Imprimir el título del video descargado
        print("Descargando video: " + video.title)

        # Descargar el video en formato MP3
        video.streams.filter(only_audio=True).first().download("./mp3")
        
        # Agregar un retraso para asegurar que la descarga se complete
        time.sleep(10)  # Puedes ajustar el tiempo según la duración de la descarga

        # Obtener el archivo MP3
        #file = mutagen.File("./mp3/" + video.title + ".mp3")
        #file = mutagen.File('"' + "./mp3/" + video.title + ".mp3" + '"')
        #file = mutagen.File("./mp3/" + video.title.replace(" ", "_") + ".mp3")
        #print("file: ", file)
        
        quoted_file_name = shlex.quote(video.title + ".mp3")
        # Crear la ruta completa del archivo
        file = "./mp3/" + quoted_file_name
        #file = EasyID3("./mp3/" + quoted_file_name)
        print("file: ", file)
        
        # Obtener el archivo MP3
        #file_path = "./mp3/" + video.title.replace(" ", "_") + ".mp3"
        #file = mutagen.File(file_path)
        #print("Ruta del archivo:", file_path)  # Agrega esta línea para verificar la ruta del archivo
        
        
        
        #file_path = "./mp3/" + video.title.replace(" ", "_") + ".mp3"
        #print("Ruta del archivo:", file_path)  # Verificar la ruta del archivo antes de intentar abrirlo
        #
        #if os.path.exists(file_path):
        #    try:
        #        file = mutagen.File(file_path)
        #        # Continuar con la manipulación de metadatos
        #    except mutagen.MutagenError as e:
        #        print("Error al abrir el archivo con Mutagen:", e)
        #else:
        #    print(f"El archivo {file_path} no existe.")
        
        # Agregar el campo "Título"
        file["title"] = video.title
        
        # Agregar el campo "Interpretes colaboradores"
        if video.author:
            file["artist"] = video.author
        else:
            file["artist"] = video.uploader
        
        # Agregar el campo "Interprete del album"
        file["albumartist"] = video.uploader

        ## Agregar el campo "Título"
        #file["title"] = video.title.replace(" ", "_")
        #
        ## Agregar el campo "Interpretes colaboradores"
        #if video.author:
        #    file["artist"] = video.author.replace(" ", "_")
        #else:
        #    file["artist"] = video.uploader.replace(" ", "_")
        #
        ## Agregar el campo "Interprete del album"
        #file["albumartist"] = video.uploader.replace(" ", "_")
        
        # Guardar los metadatos
        file.save()
