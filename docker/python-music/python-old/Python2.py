# -*- coding: utf-8 -*-

import pytube

# Obtener el URL de la lista de reproducción
playlist_url = "https://www.youtube.com/playlist?list=PLV0-i_rHNhfayEhTnncgEVAASKaxO8KuZ"

# Crear un objeto de playlist
playlist = pytube.Playlist(playlist_url)

# Obtener una lista de los videos de la playlist
videos = playlist.videos

# Iterar sobre los videos
for video in videos:
    # Descargar el video en formato MP3
    video.streams.filter(only_audio=True).first().download("./mp3")
