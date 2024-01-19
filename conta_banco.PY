from abc import ABC, abstractclassmethod





class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def setter_nome(self,valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def setter_idade(self,valor):
        self._idade = valor




class Conta(ABC):
    @abstractclassmethod
    def saque(self):
        ...

class ContaPoupanca(Conta):#Criação da conta poupança 
    def __init__(self,agencia, num_conta ,saldo=0):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo


    def saque(self,valor,agencia,num_conta):#Função saque para descontar valor do saldo, sEM extra de R$1000
        
        if agencia != self.agencia or num_conta != self.num_conta:
            print('Sua agencia ou numero da conta estão errados')
        
        elif self.saldo <= 0:
            print('Limite extra ja foi sacado')
        
        else:
            self.saldo -= valor
            print('Você sacou')
            print('Saldo R$',self.saldo)
            print()

    def depositar(self,valor,agencia,num_conta):#Função depósito para acrescentar valor ao saldo
        
        if agencia != self.agencia or num_conta != self.num_conta:
            print('Conta não encontrada para deposito')
        else:
            self.saldo += valor
            print('Você depositou')
            print('Saldo R$',self.saldo)
            print()


class ContaCorrente(Conta):#Criação da conta corrente
    def __init__(self,agencia, num_conta ,saldo=0):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    def saque(self,valor,agencia,num_conta):#Função saque para descontar valor do saldo, com extra de R$1000
        
        if agencia != self.agencia or num_conta != self.num_conta:
            print('Sua agencia ou numero da conta estão errados')
        
        elif self.saldo <= -1000:
            print('Limite extra ja foi sacado')
        
        else:
            self.saldo -= valor
            print('Você sacou')
            print('Saldo R$',self.saldo)
            print()

    def depositar(self,valor,agencia,num_conta):#Função depósito para acrescentar valor ao saldo
        
        if agencia != self.agencia or num_conta != self.num_conta:
            print('Conta não encontrada para deposito')
        else:
            self.saldo += valor
            print('Você depositou')
            print('Saldo R$',self.saldo)
            print()




user1 = ContaCorrente('bradesco',1)
user1.depositar(1000,'bradesco',1)
user1.saque(500,'bradesco',1)


