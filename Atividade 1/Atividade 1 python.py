import requests
import requests_cache
from bs4 import BeautifulSoup


def requisicao_salvamento_links(link):
    requests_cache.install_cache("bd") #instala a cache e evita o bloqueio
    response = requests.get(link) #pega o link

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

    return salvos

alvo = input("Digite um link: ")
lista_de_links = requisicao_salvamento_links(alvo)

opcao = int(input("Digite um valor: "))
palavra = input("Digite uma palavra chave: ")

requests_cache.install_cache("novo")
resposta = requests.get(f"https://www.reddit.com{lista_de_links[opcao-1]}")
contador = 0
lista_de_chave = []
if resposta.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    aparicoes = soup.get_text()
    for x in aparicoes.split():
        if palavra in x:
            contador += 1
            lista_de_chave.append(palavra)
    
    print(f"A {palavra}, aparece {contador} vezes")
else:
    print(resposta.status_code)


#print()
#print(lista_de_chave)

