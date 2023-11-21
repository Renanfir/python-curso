possiveis = '+-*/'
while True:
    num_1 = float(input("Digite o 1° numero: "))
    num_2 = float(input("Digite o 2° numero: "))
    
    operacao = input("Digite a operação, opções(+,-,/,*)")

    if num_1.isdigit() is False or num_2.isdigit() is False:
        print("Valor inválido!")
        continue
    
    if operacao not in possiveis or len(operacao) > 1:
        print("operação impossivel!")
        continue
    
    if operacao == '+':
        print("Resultado:",num_1+num_2)
    elif operacao == '-':
        print("Resultado:",num_1-num_2)
    elif operacao == '*':
        print("Resultado:",num_1*num_2)
    elif operacao == '/':
        print("Resultado:",num_1/num_2)
    
    sair = input("Deseja sair? ")
    if sair.lower().startswith('s'):
        print("você saiu")
        break
