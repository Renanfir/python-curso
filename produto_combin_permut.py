from itertools import product,permutations,combinations

camisetas = [['preta','Branca'],
             ['P','M','G','GG'],
             ['Masc','Femi','unix'],
             ['alg','poli']]

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
    
def print_combinacao(lista):
    print(*list(combinations(lista,2)),sep="\n")
    print()

print_combinacao(pessoas)

def print_permutacao(lista):
    print(*list(permutations(lista,)),sep="\n")
    print()

print_permutacao(pessoas)

def print_produto(lista):
    print(*list(product(*lista)), sep="\n")
    print()
    
print_produto(camisetas)