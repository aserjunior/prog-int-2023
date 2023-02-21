import requests
from bs4 import BeautifulSoup

# cep = '06233-030'
colocar_cep = str(input('Insira o CEP no formato xxxxx-xxx:\n'))

# url = 'https://cdn.apicep.com/file/apicep/' + cep + '.json'
url_especifico = 'https://cdn.apicep.com/file/apicep/' + colocar_cep + '.json'
response = requests.get(url_especifico)
print(response.text)
