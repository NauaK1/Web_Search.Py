import sys
import re

import requests
from bs4 import BeautifulSoup

REGEX = {
    "emails": r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    "telefones_br": r'^(\(?\d{2}\)?)\s?(9?\d{4}-\d{4}|\d{4}-\d{4})$',
    "nomes": r'^[A-Za-zÀ-ÖØ-öø-ÿ’\']+(?:\s+[A-Za-zÀ-ÖØ-öø-ÿ’\']+)+$',
    "CPF": r'^(?:\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$',
    "CNPJ": r'^(?:\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}|\d{14})$',
    "CPF_ocultos": r'^[0-9*]{3}\.[0-9*]{3}\.[0-9*]{3}-[0-9*]{2}$'
}

email = "kauan@gmail.com"
if re.fullmatch(REGEX["emails"], email):
    print("E")


"""link = "http://google.com.br"

resposta = requests.get(link)
if resposta.status_code == 200:
    html_doc = resposta.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    
    for link in soup.find_all('a'):
        print(link.get("href"))
    
    print(soup.get_text())

else:
    print("Não foi possivel acessar o html desse link")"""



if __name__ == "__main__":
    
    print("""
 _ _ _ _____ ___     _____ _____ _____ _____ _____ _____     _____ __ __ 

| | | |   __| __|   |   __|   __|  _  | __  |     |  |  |   |  _  |  |  |
| | | |   __|__ |   |__   |   __|     |    _|-   -|  |  |   |   __|_   _|
|_____|_____|___|   |_____|_____|__|__|__|__|_____|_____|   |__|    |_|  
                                                                         
""")
print("              ┌──────────────────────────────────┐")
print("              │          web.search.py           │")
print("              │        Developed by Nauak        │")
print("              └──────────────────────────────────┘")

