import os
lista = []
lista_desfazer = []

print("---------------------------------------------")
print("|                OPÇÕES                     |")
print("|   PARA ADICIONAR BASTA DIGITAR A TAREFA   |")
print("|   PARA SAIR DIGITE SAIR                   |")
print("|   1 - MOSTRA                              |")
print("|   2 - REMOVER                             |")
print("|   3 - DESFAZER                            |")
print("---------------------------------------------")
print()

opcao = 1
while opcao != 'SAIR': #enquanto a opção for diferente de 0, mostra, add, remover, desfazer, rode o programa em loop
    
    #input da opção
    opcao = str(input(f'Digite "{"SAIR"}" para sair ou uma tarefa para ser adicionada: '))

    #opção de listagem
    if opcao == '1':
        if not lista:
            print("não há nada para listar")
        elif lista:
            for i in lista:
                print(i)


    #opção de adicionar item
    elif opcao != 'SAIR' and opcao != '1' and opcao != '2' and opcao != '3':
        lista.append(opcao)


    
    #opção de remoção do ultimo item
    elif opcao == '2':
        
        ultimo_removido = (lista.pop(-1))
        lista_desfazer.append(ultimo_removido)
        
        if not lista:
            try:
                ...
            except:
                print("não há nada para remover")



    #opção de desfazer retirada
    elif opcao == '3':
        lista.append(lista_desfazer[-1])
        lista_desfazer.pop(-1)
        
        if not lista:
            try:
                ...
            except:
                print("não há nada para desfazer")
        
        
print("saiu do programa!")
