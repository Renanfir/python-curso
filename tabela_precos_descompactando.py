produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


novo_produto = [{**produto, 'nome':produto['nome'], 'preco': produto['preco']*2}
                 
                 if produto['preco'] > 20
                 else {**produto}
                
                for produto in produtos]
print(*novo_produto, sep='\n')