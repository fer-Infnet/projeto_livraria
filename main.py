# Exercício 5
import requests
from bs4 import BeautifulSoup
import csv  

# Exercício 6
url = "http://books.toscrape.com/"
resposta = requests.get(url)

# Exercício 7
if resposta.status_code == 200:
    print("Conexão bem-sucedida!")
else:
    print("Erro na conexão:", resposta.status_code)
    exit()

# Exercício 8
soup = BeautifulSoup(resposta.text, "html.parser")
print(soup.title)

# Exercício 9
livros_html = soup.find_all("article", class_="product_pod")

# Exercício 10
print(len(livros_html))  # Deve imprimir 20

# Exercício 11
dados_extraidos = []
for livro in livros_html:
    # Exercício 12: título
    titulo = livro.h3.a["title"]

    # Exercício 13: preço
    preco = livro.find("p", class_="price_color").text

    # Exercício 14: dicionário
    dados_extraidos.append({"titulo": titulo, "preco": preco})

print(dados_extraidos)  # lista com os 20 dicionários

# Exercício 15 e 16
with open("relatorio_livros.csv", "w", newline="", encoding="utf-8") as arquivo:
    gravador = csv.DictWriter(arquivo, fieldnames=["titulo", "preco"])
    gravador.writeheader()
    gravador.writerows(dados_extraidos)

print("Relatório CSV gerado com sucesso!")