caminho_arquivo = 'testando_samerda.txt'

with open(caminho_arquivo ,'w+') as arquivo:
    arquivo.write("l1\n")
    arquivo.write("l2\n")
    arquivo.write("l3\n")
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())