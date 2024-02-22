lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

# Verifica o tipo dos dados
for item in lista:

    if isinstance(item, set):
        print(item, ' - set')

    elif isinstance(item, str):
        print(item, ' - string')

    elif isinstance(item, (float, int)):
        print(item, ' - Numero')

    elif isinstance(item, tuple):
        print(item, ' - tupla')

    elif isinstance(item, list):
        print(item, ' - lista')

    else:
        print(item,' - Outro')

    

