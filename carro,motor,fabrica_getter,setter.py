class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabrica = None

    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def setter_motor(self,valor):
        self._motor = valor


    @property
    def fabrica(self):
        return self._fabrica
    
    @fabrica.setter
    def setter_fabrica(self,valor):
        self._fabrica = valor

class Motor:
    def __init__(self,nome):
        self.nome = nome
        

class Fabrica:
    def __init__(self,nome):
        self.nome = nome


fusca = Carro('Fusca')
motor = Motor('1300')
fabrica = Fabrica('Volks')
fusca.setter_motor = motor
fusca.setter_fabrica = fabrica
print(fusca.nome, fusca.motor.nome, fusca.fabrica.nome)
    








        