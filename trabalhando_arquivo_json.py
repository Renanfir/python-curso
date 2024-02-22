import json
import os.path
from pprint import pprint
from typing import TypedDict

NOME_ARQUIVO = 'arquivo.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(os.path.join(os.path.dirname(__file__), NOME_ARQUIVO))
print(os.path.dirname(__file__))


# Criando uma classe com atributos nomeados
class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None

# Adicionando conteudo aos atributos
filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001, 'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None,
}

# Criand oarquivo json e colando a variável filme
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

# Carregando a variavel filme do arquivo
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)

print(filme_do_json)