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

def mostra(lista):
    if not lista:
        print("Não há nada para apresentar")
        return
    print(lista)

def remove(lista):
    if not lista:
        print("Não há nada para remover")
        return
    removido = lista.pop(-1)
    lista_desfazer.append(removido)

def desfaz(lista):
    if not lista:
        print("Não há nada para desfazer")
        return
    lista.append(lista_desfazer[-1])
    lista_desfazer.pop(-1)


opcao = 1
while opcao != 'SAIR': #enquanto a opção for diferente de 0, mostra, add, remover, desfazer, rode o programa em loop
    
    #input da opção
    opcao = str(input(f'Digite "{"SAIR"}" para sair ou uma tarefa para ser adicionada: '))

    #opção de listagem
    if opcao == '1':
        mostra(lista)


    #opção de adicionar item
    elif opcao != 'SAIR' and opcao != '1' and opcao != '2' and opcao != '3':
        lista.append(opcao)

    #opção de remoção do ultimo item
    elif opcao == '2':
        remove(lista)
        

    #opção de desfazer retirada
    elif opcao == '3':
        desfaz(lista)
        
        
print("saiu do programa!")
