import requests
import requests_cache
from bs4 import BeautifulSoup



requests_cache.install_cache("bd") #instala a cache e evita o bloqueio
response = requests.get("https://www.reddit.com/r/nhaa/") #pega o link

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser") #deixa bunito
    lista_de_links = soup.select("a") #filtra por links
    lista_de_links = lista_de_links[:10] #cria uma lista com 10 de len
    salvos = []

    i = 1
    
    for link in lista_de_links:
        print(f"{i} = ", link["href"]) #printa cada link, agora falta só pegar os títulos
        i += 1
        salvos.append(link["href"]) #salva os links em uma lista

else:
    print(response.status_code)

opcao = int(input("Digite um valor: "))
palavra = input("Digite uma palavra chave: ")

resposta = requests.get(f"https://www.reddit.com{salvos[opcao-1]}")
contador = 0
lista_de_chave = []
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    aparicoes = soup.get_text()
    for x in aparicoes.split():
        if palavra in x:
            contador += 1
            lista_de_chave.append(palavra)
    
    print(f"A {palavra}, aparece {contador} vezes")
else:
    print(response.status_code)


#print()
#print(lista_de_chave)

