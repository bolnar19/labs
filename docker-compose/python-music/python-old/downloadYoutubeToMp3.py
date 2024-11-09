# -*- coding: utf-8 -*-

import pytube
import sys
import re
import shlex
#import ssl

# Desactivar la verificación del certificado SSL
#ssl._create_default_https_context = ssl._create_unverified_context

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
start_index = 1220
#start_index = 915
#start_index = 923
#start_index = 951
#start_index = 1030


# Iterar sobre los videos
#for index, video in enumerate(videos):
#    if index >= start_index:
#            
#        # Imprimir el título del video descargado
#        print("Descargando video: " + video.title)
#
#        # Descargar el video en formato MP3
#        video.streams.filter(only_audio=True).first().download("./mp3")


# Iterar sobre los videos
for index, video in enumerate(videos):
    if index >= start_index:
        try:
            # Descargar el audio en formato MP3 con el nombre del autor y del título de la canción
            filename = f"{video.author} - {video.title}"
            #audio_stream.download(output_path="./mp3", filename=filename)
        
            # Limpiar el nombre del video para eliminar caracteres no permitidos en el nombre del archivo
            cleaned_title = clean_filename(filename)
            # Imprimir el título del video descargado
            #print("Descargando video: " + video.author + " - " + video.title)
            #print("Descargando video: " + video.author.encode('utf-8').decode('utf-8') + " - " + video.title.encode('utf-8').decode('utf-8'))
            # Imprimir el título del video descargado
            print("Descargando video " + str(start_index) + ": " + cleaned_title)
            
            #sys.stdout.flush()  # Forzar la impresión inmediata
            
            # Obtener la URL del audio en formato MP3
            audio_stream = video.streams.filter(only_audio=True).first()
            
            # Descargar el audio en formato MP3 con el nombre original del video
            #audio_stream.download(output_path="./mp3", filename=video.title + ".mp3")
        


            # Descargar el video en formato MP4
            #video.streams.filter(only_audio=True).first().download("./mp3")
            #audio_stream.download("./mp3", filename=f"{video.title}.mp3")
            
            # Descargar el audio en formato MP3 con el nombre limpio
            audio_stream.download("./mp3", filename=f"{cleaned_title}.mp3")
            #audio_stream.download(output_path="./mp3", filename=filename)
        except pytube.exceptions.AgeRestrictedError:
            print(f"El video '{video.title}' está restringido por edad.")
            input("Presiona Enter para continuar después de descargar manualmente o presiona cualquier tecla para omitir: ")
