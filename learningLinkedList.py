class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.cabeca = None

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")


    def inserir_inicio(self, valor):
        novo_no = Node(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def inserir_fim(self, valor):
        novo_no = Node(valor)

        if not self.cabeca:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no


lista = LinkedList()
lista.inserir_inicio(1)
lista.inserir_inicio(2)
lista.inserir_inicio(3)
lista.exibir()
