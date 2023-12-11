import os
import json

pessoa = {
    'nome': 'Reno',
    'sobrenome' : 'Souza',
    'enderecos': [
        {'rua':'R1', 'numero':32},
        {'rua':'R2', 'numero':55}
    ],
    'altura': 1.9,
    'numeros_pref': (2,4,6,8,10),
    'dev': True,
    'nada': None,
}

with open('aula4983.json', 'w+') as arquivo:
    json.dump(pessoa, arquivo, indent = 2)

with open('aula4983.json', 'r', encoding="utf-8") as arquivo:
    pessoa = json.load(arquivo)

print(pessoa)
