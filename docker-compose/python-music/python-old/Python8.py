
from mutagen.easyid3 import EasyID3

mp3_filename_import = 'Ed Maverick - Ropa De Bazar.mp3'

audio = EasyID3(mp3_filename_import)
audio['title'] = "Title"
audio['artist'] = "Artist"
audio['album'] = "Album"
audio['composer'] = "" # empty
audio.save()