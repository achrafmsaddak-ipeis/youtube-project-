from __future__ import unicode_literals
import youtube_dl

mylist = ['https://www.youtube.com/watch?v=NEqHPxnxrFc',
                'https://www.youtube.com/watch?v=BHCWFzQlQrk',
                'https://www.youtube.com/watch?v=BQN8-roIzuo']
result = []


ydl_opts = {'format': 'bestaudio/best',
            'outtmpl': 'C:/Users/Achraf/Videos/for testing/%(title)s.%(ext)s',
            'download_archive': 'downloaded_songs.txt',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',}],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(mylist)
    
#for url in mylist :
#    result.append(ydl.extract_info(url,False))

ydl = youtube_dl.YoutubeDL()
urls = ydl.extract_info('https://www.youtube.com/playlist?list=PLFQnTObKN6yu_k6Yp3G4zRenAv3Kj0Bwx',False)['entries']

print(urls)