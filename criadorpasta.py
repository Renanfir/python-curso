caminho_arquivo = 'pasta_criada.txt'

# Abrindo e escrevendo em um arquivo
with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write("l1\n")
    arquivo.write("l2\n")
    arquivo.write("l3\n")
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())
