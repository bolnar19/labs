# -*- coding: utf-8 -*-

import pytube
import sys
import re
import mutagen

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def clean_filename(name):
    # Reemplazar caracteres no permitidos con un guion bajo
    cleaned_name = re.sub(r'[<>:"/\\│|?*]', ' ', name)
    return cleaned_name

# Obtener el URL de la lista de reproducción
playlist_url = "https://www.youtube.com/playlist?list=PLV0-i_rHNhfayEhTnncgEVAASKaxO8KuZ"

# Crear un objeto de playlist
playlist = pytube.Playlist(playlist_url)

# Obtener una lista de los videos de la playlist
videos = playlist.videos

# Obtener el índice del video a partir del que se desea comenzar la descarga
#start_index = 915
#start_index = 923
start_index = 923

# Iterar sobre los videos
for index, video in enumerate(videos):
    if index >= start_index:
        try:
            # Descargar el audio en formato MP3 con el nombre del autor y del título de la canción
            filename = f"{video.author} - {video.title}"
        
            # Limpiar el nombre del video para eliminar caracteres no permitidos en el nombre del archivo
            cleaned_title = clean_filename(filename)

            # Imprimir el título del video descargado
            print("Descargando video " + str(start_index) + ": " + cleaned_title)

            sys.stdout.flush()  # Forzar la impresión inmediata
            
            # Obtener la URL del audio en formato MP3
            audio_stream = video.streams.filter(only_audio=True).first()
            
            # Descargar el audio en formato MP3 con el nombre limpio
            audio_stream.download("./mp3", filename=f"{cleaned_title}.mp3")

        except pytube.exceptions.AgeRestrictedError:
            print(f"El video '{video.title}' está restringido por edad.")
            input("Presiona Enter para continuar después de descargar manualmente o presiona cualquier tecla para omitir: ")

        cleaned_file_name = clean_filename(filename + ".mp3")
        print("*** Var cleaned_file_name: ", cleaned_file_name)
        
        file_path = "./mp3/" + cleaned_file_name

        # Verificar si existe cabecera ID3
        try:
            file = EasyID3(file_path)
            print("*** Var file try: ", file)
        except mutagen.id3._util.ID3NoHeaderError:
            # Crear una nueva cabecera ID3
            file = EasyID3()
            print("*** Var file except: ", file)
    
        # Agregar el campo "Título"
        print("*** Var file despues: ", file)
        file["title"] = video.title

        # Guardar los metadatos
        print("*** Var file: ", file)
        #file.save()
        
        # Agregar el campo "Interpretes colaboradores"
        if video.author:  
            file["artist"] = video.author
        else:
            file["artist"] = video.author
        
        # Agregar el campo "Interprete del album"
        file["albumartist"] = video.author
        
        # Guardar los metadatos
        file.save()
