import eyed3 
import metadata
import scarping

def taggin_process():

    folder_title = scarping.palylist_title
    newpath = 'C:/Users/Achraf/Music/%s' % folder_title  

    for song in metadata.songs :

        title_name = song['title']
        bad_chars = ['|', '?', ':', '!', "*", '"', '<', '>']
        title_name = ''.join(i for i in title_name if not i in bad_chars) 
        filename = newpath + '/' + title_name + '.mp3'
    
        audiofile = eyed3.load(filename)
        if (audiofile.tag == None):
            audiofile.initTag()

        audiofile.tag.artist = song['artist']
        audiofile.tag.album = song['album']
        if song['track'] == None :
            audiofile.tag.title = song['track'] 
        else :
            audiofile.tag.title = song['track']
        try :
            audiofile.tag.images.set(3, open(newpath + '/' + title_name + '.jpg','rb').read(), 'image/jpeg')
        except :
            print('file not found')

        audiofile.tag.save()



