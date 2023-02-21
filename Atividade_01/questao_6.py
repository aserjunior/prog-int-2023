import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.meutimao.com.br/tabela-de-classificacao/campeonato_brasileiro/')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find(class_='tabela_principal')
print(links.text)