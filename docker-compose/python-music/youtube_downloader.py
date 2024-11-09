# youtube_downloader.py
import yt_dlp
import os

def download_audio(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Guarda en la carpeta "downloads"
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == "__main__":
    # URL de YouTube de ejemplo
    youtube_url = input("Introduce el enlace de YouTube: ")
    download_audio(youtube_url)
