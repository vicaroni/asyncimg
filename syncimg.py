from urllib.request import urlopen
from re import findall

urls = [
'https://www.evonove.it',
'http://www.moto.it',
'https://it.wikipedia.org/wiki/Immagine',
'https://pixabay.com',
'https://www.shutterstock.com',
]
for url in urls:
    print(url)
    imgs = findall('\<img[^\<\>]+src="([^\"]*)', str(urlopen(url).read()))
    for img in imgs:
        print('\t'+img)
