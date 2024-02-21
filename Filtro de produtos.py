import copy
from dadosexec import produtos

#Aumentando 10% do preço do produto
produtos_novos = [{**produto, 'nome':produto['nome'], 
                   'preco': round(produto['preco']*1.1, 2)}
                    
                    for produto in copy.deepcopy(produtos)]

#Ordenando os preços 
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

#Ordenando os nomes 
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)

#Saída
print(*produtos_novos, sep="\n")
print()
print(*produtos_ordenados_por_preco, sep="\n")
print()
print(*produtos_ordenados_por_nome, sep="\n")
