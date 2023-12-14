import json

class Pessoa:
    def __init__(self, nome, idade, tamanho) -> None:
        self.nome = nome
        self.idade = idade
        self.tamanho = tamanho


p1 = Pessoa(
    'Renan',
    16,
    190,
)

with open('arquivo.json','w') as arquivo:
    json.dump(p1.__dict__, arquivo, indent=2)
