import json

with open('arquivo.json', 'r') as arquivo:
    dados_pessoa = json.load(arquivo)

print(dados_pessoa)