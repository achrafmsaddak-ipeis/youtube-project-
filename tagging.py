
import eyed3 
import metadata
import scarping

folder_title = scarping.palylist_title
newpath = 'C:/Users/Achraf/Music/%s' % folder_title  

for song in metadata.songs :

    title_name = song['title']
    for i in range(len(title_name)) :
        if title_name[i] in ['/','|','*']:
            title_name = title_name[:i]+ '_' + title_name[i+1:]
        if title_name[i] in [':'] :
            title_name = title_name[:i]+ '-' + title_name[i+1:]
    bad_chars = ['?', '!', '"', '<', '>']
    title_name = ''.join(i for i in title_name if not i in bad_chars) 
    filename = newpath + '/' + title_name + '.mp3'

    try :
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
            audiofile.tag.images.set(3, open(newpath + '/' + str(metadata.songs.index(song)) + '.jpg','rb').read(), 'image/jpeg')
        except :
            print('file not found')

        audiofile.tag.save()
    except :
        print('passed over',title_name)



