import os
from pathlib import Path


caminho_arquivo = Path(__file__)

# Tenta criar arquivo e caso ja exista manda mensagem de erro
try:
    os.mkdir(caminho_arquivo.parent / 'teste')
except FileExistsError:
    print('exist_ok = true não funciona')

# Criando arquivo dentro da pasta crida
arquivo = caminho_arquivo.parent / 'teste'
criar_arquivo = arquivo / 'arquivo_escrita.txt'

criar_arquivo.touch(exist_ok=True)

