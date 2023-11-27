import copy
from dadosexec import produtos


produtos_novos = [{**produto, 'nome':produto['nome'], 
                   'preco': round(produto['preco']*1.1, 2)}
                    
                    for produto in copy.deepcopy(produtos)]


produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)

print(*produtos_novos, sep="\n")
print()
print(*produtos_ordenados_por_preco, sep="\n")
print()
print(*produtos_ordenados_por_nome, sep="\n")
