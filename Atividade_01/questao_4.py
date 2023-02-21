import requests
from bs4 import BeautifulSoup

imagem = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz8wxi7nITDrpNAacciAbw3jVgmTUJ42Z5Hg&usqp=CAU'

response = requests.get(imagem)

fp = open('psyduck.png', 'wb')
fp.write(response.content)
fp.close()