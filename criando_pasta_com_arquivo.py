import os
from pathlib import Path


caminho_arquivo = Path(__file__)

try:
    os.mkdir(caminho_arquivo.parent / 'teste')
except FileExistsError:
    print('exist_ok = true não funciona')

arquivo = caminho_arquivo.parent / 'teste'
criar_arquivo = arquivo / 'arquivo_escrita.txt'

criar_arquivo.touch(exist_ok=True)

