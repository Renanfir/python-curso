possiveis = '+-*/'
while True:

    # Adicionando numeros
    num_1 = float(input("Digite o 1° numero: "))
    num_2 = float(input("Digite o 2° numero: "))
    
    operacao = input("Digite a operação, opções(+,-,/,*)")

    # Verifica se é um número
    if num_1.isdigit() is False or num_2.isdigit() is False:
        print("Valor inválido!")
        continue
    
    if operacao not in possiveis or len(operacao) > 1:
        print("operação impossivel!")
        continue

    # Verifica operação
    if operacao == '+':
        print("Resultado:", num_1+num_2)
    elif operacao == '-':
        print("Resultado:", num_1-num_2)
    elif operacao == '*':
        print("Resultado:", num_1*num_2)
    elif operacao == '/':
        print("Resultado:", num_1/num_2)

    # Verifica saída
    sair = input("Deseja sair? ")
    if sair.lower().startswith('s'):
        print("você saiu")
        break
