from __future__ import unicode_literals
import os
import youtube_dl
import scarping


songs = [] 
ydl = youtube_dl.YoutubeDL()
for url in scarping.urls :
    songs.append({})
    meta = ydl.extract_info(url,False)
    songs[-1]['title'] = meta['title'] 
    songs[-1]['id'] = meta['id']
    if 'track' in meta.keys() :
        songs[-1]['track'] = meta['track']
    if 'artist' in meta.keys() :
        songs[-1]['artist'] = meta['artist']
    if 'album' in meta.keys() :
        songs[-1]['album'] = meta['album']
    if 'release_date' in meta.keys() :
        songs[-1]['release_date'] = meta['release_date']
    if 'release_year' in meta.keys() :
        songs[-1]['release_year'] = meta['release_year']
    songs[-1]['cover'] = 'https://i.ytimg.com/vi/%s/maxresdefault.jpg' % meta['id']

metafile = open("meta.txt","w",encoding="utf-8") 
metafile.write("the metadata of the downlaoded songs") 
metafile.write("\n") 
metafile.close()

for song in songs :
    metafile = open("meta.txt","a",encoding="utf-8") 
    for key in song.keys() :
        metafile.write(key + ' : ' + str(song[key]))
        metafile.write("\n")
    metafile.write("\n")
    metafile.close()