import requests
from bs4 import BeautifulSoup

url = 'http://www.google.com/search'

conteudo_buscado = str(input("Insira o que quer buscar:\n"))

nova_string = conteudo_buscado.replace(" ", "+")

q = "?q=" + nova_string

url_buscar = url + q

response = requests.get(url_buscar)
print(response.status_code)