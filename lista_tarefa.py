import os
lista = []

print("-------------------------")
print("|        OPÇÕES          |")
print("|0 - SAIR                |")
print("|1 - MOSTRA LISTA        |")
print("|2 - ADD                 |")
print("|3 - REMOVER ULTIMO      |")
print("|4 - DESFAZER UMA REMOÇÃO|")
print("-------------------------")
print()

opcao = 1
while opcao != 0: #enquanto a opção for diferente de 0 rode o programa em loop
    
    #input da opção
    opcao = int(input("Digite algo que precisa fazer e 0 para sair do programa: "))

    #opção de listagem
    if opcao == 1:
        if not lista:
            print("não há nada para listar")
        elif lista:
            for i in lista:
                print(i)
    
    #opção de adicionar item
    elif opcao == 2:
        add = str(input("Digite oque deseja fazer: "))
        lista.append(add)

    
    #opção de remoção do ultimo item
    elif opcao == 3:
        ultimo_removido = (lista.pop(-1))
        
        if not lista:
            try:
                ...
            except:
                print("não há nada para remover")

    
    #opção de desfazer retirada
    elif opcao == 4:
        lista.append(ultimo_removido)
        
        if not lista:
            try:
                ...
            except:
                print("não há nada para desfazer")
        
        
print("saiu do programa!")
