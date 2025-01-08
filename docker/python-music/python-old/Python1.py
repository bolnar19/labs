# -*- coding: utf-8 -*-

from pytube import YouTube
from moviepy.editor import *

# URL del video de YouTube
url = 'https://www.youtube.com/watch?v=YUm-LpX1vvY&list=PLV0-i_rHNhfayEhTnncgEVAASKaxO8KuZ&index=118'

# Descarga el video utilizando pytube
yt = YouTube(url)
video = yt.streams.filter(only_audio=True).first()
video.download(filename='temp')

# Convierte el video descargado a MP3
video_clip = AudioFileClip('temp.mp4')
video_clip.write_audiofile('output.mp3')

# Elimina el archivo de video temporal
video_clip.close()
os.remove('temp.mp4')

#print("¡Descarga y conversión exitosas!")
