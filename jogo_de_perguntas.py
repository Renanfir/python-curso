perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertou = None
certas = 0
for pergunta in perguntas:
    print()
    print(pergunta['Pergunta'])

    opcoes = pergunta['Opções']
    for i,opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    
    escolha = int(input("Digite a opção certa: "))

    qnt_opcoes = len(opcoes)
    if escolha >= 0 and escolha < qnt_opcoes:
        if opcoes[escolha] == pergunta['Resposta']:
            acertou = True

    if acertou:
        print("Você acertou")
        certas +=1
    else:
        print("Não acertou")
print("Você acertou ",certas)
    