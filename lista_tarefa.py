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
while opcao != "0":
    
    
    opcao = int(input("Digite algo que precisa fazer e 0 para sair do programa: "))
    
    if opcao == 1:
        if not lista:
            print("não há nada para listar")
        elif lista:
            for i in lista:
                print(i)
    
    elif opcao == 2:
        add = str(input("Digite oque deseja fazer: "))
        lista.append(add)


    elif opcao == 3:
        if not lista:
            try:
                ultimo_removido = (lista.pop(-1))
            except:
                print("não há nada para remover")


    elif opcao == 4:
        if not lista:
            try:
                lista.append(ultimo_removido)
            except:
                print("não há nada para desfazer")
        
        
print("saiu do programa!")
