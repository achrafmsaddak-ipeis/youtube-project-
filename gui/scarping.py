from bs4 import BeautifulSoup
import requests

#the url of the YouTube playlist
#the playlist must not be private or else errors will occur
url = 'https://www.youtube.com/playlist?list=PLFQnTObKN6yu_k6Yp3G4zRenAv3Kj0Bwx'


def extract_data(url) :
    '''Usuing BeautifulSoup  and request to parse and crawl the playlist HTML to extract the playlist name and the URLs of its videos
    The output of the function is the playlist title and a list of the URLs '''

    req = requests.get(url)
    soup = BeautifulSoup(req.text,'lxml')

    #the playlist name 
    palylist_title = soup.findAll(class_ = 'pl-header-title')[0].text
    palylist_title = palylist_title.strip()

    #the list of the URLs
    urls = []
    table = soup.findAll(class_ = 'pl-video-title')
    for vid in table :
        adress = 'https://www.youtube.com'+vid.a['href']
        ind = adress.find('&list=')
        urls.append(adress[0:ind])
        

    return palylist_title , urls

def downlaod_img(url,folder,name) :
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(folder + '/' + name + '.jpg', 'wb') as img:
            for chunk in response.iter_content():
                img.write(chunk)

palylist_title , urls = extract_data(url)