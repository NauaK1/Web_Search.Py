import re
import time
import threading

import requests
from bs4 import BeautifulSoup

REGEX = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,24}",
    "telefones_br": r'\+55\s?\d{2}\s?\d{4,5}\s?\d{4}|\(?\d{2}\)?\s?9?\s?\d{4}[-\s]?\d{4}',
    "nomes": r'[A-Za-zÀ-ÖØ-öø-ÿ’\']+(?:\s+[A-Za-zÀ-ÖØ-öø-ÿ’\']+)+',
    "CPF": r'(?:\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})',
    "CNPJ": r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}|\d{14}',
    "CPF_ocultos": r'[0-9*]{3}\.[0-9*]{3}\.[0-9*]{3}-[0-9*]{2}'
}

TOCRAWLER = []
CRAWLED = set()


def buscar_telefone(url):
    telefones = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        resposta = requests.get(url, headers=headers, timeout=10)
        
        if resposta.status_code == 200:
            html = resposta.text

            encontrados = re.findall(REGEX['telefones_br'], html)
            for tel in encontrados:
                print(f"Telefone encontrado: {tel}")
                telefones.append(tel)
        elif resposta.status_code != 404:
            print("Não foi possivel acessar a pagina")
                
    except Exception as e:
        print(f"Erro ao acessar a URL {url}: {e}")
    
    return telefones


def buscar_email(url):
    emails = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        resposta = requests.get(url, headers=headers, timeout=10)
        
        if resposta.status_code == 200:
            html = resposta.text

            encontrados = re.findall(REGEX['emails'], html)
            for email in encontrados:
                print(f"E-mail encontrado: {email}")
                emails.append(email)
        elif resposta.status_code != 404:
            print("Não foi possivel acessar a pagina")
                
    except Exception as e:
        print(f"Erro ao acessar a URL {url}: {e}")
    
    return emails


def buscar_cpf(url):
    cpfs = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        resposta = requests.get(url, headers=headers, timeout=10)
        
        if resposta.status_code == 200:
            html = resposta.text

            encontrados = re.findall(REGEX['CPF'], html)
            for cpf in encontrados:
                if cpf not in cpfs:
                    print(f"CPF encontrado: {cpf}")
                    cpfs.append(cpf)
        elif resposta.status_code != 404:
            print("Não foi possivel acessar a pagina")
                
    except Exception as e:
        print(f"Erro ao acessar a URL {url}: {e}")
    
    return cpfs


def buscar_cnpj(url):
    cnpjs = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        resposta = requests.get(url, headers=headers, timeout=10)
        
        if resposta.status_code == 200:
            html = resposta.text

            encontrados = re.findall(REGEX['CNPJ'], html)
            for cnpj in encontrados:
                if cnpj not in cnpjs:
                    print(f"CNPJ encontrado: {cnpj}")
                    cnpjs.append(cnpj)
        elif resposta.status_code != 404:
            print("Não foi possivel acessar a pagina")
                
    except Exception as e:
        print(f"Erro ao acessar a URL {url}: {e}")
    
    return cnpjs


def buscar_links(url):
    TOCRAWLER.append(url)
    try:
        while TOCRAWLER:
            link = TOCRAWLER.pop()
            if link not in TOCRAWLER and link not in CRAWLED:
                CRAWLED.add(link)
                resposta = requests.get(link)
                if resposta.status_code == 200:
                    html = resposta.text
                    soup = BeautifulSoup(html, 'html.parser')
            
                    for link in soup.find_all('a'):
                        href = link.get("href")
                        if href and href.startswith("http"):
                            print(f"{href} --> 200✅")
                            TOCRAWLER.append(href)
                            

                elif resposta.status_code != 404:
                    print(f"{link} --> {resposta.status_code}")


    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass

"""t1 = threading.Thread(buscar_links("http://example.com"))
t2 = threading.Thread(buscar_links("http://example.com"))

t1.start()
t2.start()

t1.join()
t2.join()
print(CRAWLED)"""
