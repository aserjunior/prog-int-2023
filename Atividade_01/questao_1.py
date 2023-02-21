import requests
import requests_cache
from bs4 import BeautifulSoup

response = requests.get('http://google.com')
print(response.status_code)
print(response.headers['content-type'])
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')

for link in links:
    buscado = link.get_text()
    print(" >>> ", buscado)