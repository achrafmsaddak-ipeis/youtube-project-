from __future__ import unicode_literals
import os
import youtube_dl
import scarping
import metadata


folder_title = scarping.palylist_title
newpath = 'C:/Users/Achraf/Music/%s' % folder_title  

if not os.path.exists(newpath):
    os.makedirs(newpath)


ydl_opts = {'format': 'bestaudio/best',
            'outtmpl': newpath + '/%(title)s.%(ext)s',
            'download_archive': 'downloaded_songs.txt',
            'quiet' : True ,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',}],
            }

print(scarping.urls)

#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
 #   ydl.download(scarping.urls)

for song in metadata.songs :
    try:
        scarping.downlaod_img(song['cover'],newpath,str(metadata.songs.index(song)))
    except :
        pass
