import requests
import requests_cache
from bs4 import BeautifulSoup

response = requests.get('http://google.com')
soup = BeautifulSoup(response.text, 'html.parser')
elemento = str(input('Insira qual tag deve ser buscada:\n'))
links = soup.find_all(elemento)

for link in links:
    buscado = link.get_text()
    print(" >>> ", buscado)