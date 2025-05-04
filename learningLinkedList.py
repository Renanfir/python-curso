class Node:
    def __init__(self, valor):
        # Valor em si
        self.valor = valor

        #Ponteiro para o proximo valor
        self.proximo = None



class LinkedList:
    def __init__(self):

        #Primeiro elemento da lista
        self.cabeca = None


    def exibir(self):
        
        #Primeiro elemento
        atual = self.cabeca

        #Enquanto o elemento atual não for None
        while atual:

            print(atual.valor, end=" -> ")
            
            #O elemento atual é igual ao proximo oque faz com que o
            #while se repita caso o proximo e agora atual não seja None
            atual = atual.proximo

        #Quanto o valor atual for none é printado none para representar o 
        #final do linked list
        print("None")



    def inserir_inicio(self, valor):

        #Novo valor
        novo_no = Node(valor)

        #O ponteiro do novo nó é apontado para o antigo primeiro elemento
        novo_no.proximo = self.cabeca

        #O primeiro elemento agora é o novo nó
        self.cabeca = novo_no



    def inserir_fim(self, valor):

        #Novo valor
        novo_no = Node(valor)

        #Verifica se o linked list possui um inicio, caso não, o novo nó é a cabeça
        if not self.cabeca:
            self.cabeca = novo_no
            return
        
        #Caso o linked list ja tenha um inicio
        atual = self.cabeca

        #Faz a verificação de elementos até encontrar o None(ultimo elemento)
        while atual.proximo:
            atual = atual.proximo

        #Quando encontrado o None, o novo nó é inserido antes dele
        atual.proximo = novo_no


lista = LinkedList()
lista.inserir_inicio(1)
lista.inserir_inicio(2)
lista.inserir_inicio(3)
lista.exibir()
