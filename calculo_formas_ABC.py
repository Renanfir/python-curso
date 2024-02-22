from abc import ABC, abstractmethod

# Criando classe abstrata
class Forma(ABC):
    @abstractmethod
    def calculo_area(self):
        ...

    @abstractmethod
    def calculo_perimetro(self):
        ...

# Criando quadrado com a forma abstrata
class Quadrado(Forma):
    def __init__(self,lado) -> None:
        super().__init__()
        self.lado = lado

    def calculo_area(self):
        return self.lado * self.lado
    
    def calculo_perimetro(self):
        return self.lado * 4


# Criando circulo com a forma abstrata
class Circulo(Forma):
    def __init__(self,raio) -> None:
        super().__init__()
        self.raio = raio

    def calculo_area(self):
        return self.raio**2 * 3.14
    
    def calculo_perimetro(self):
        return 2 * 3.14 * self.raio

circulo = Circulo(3)
quadrado = Quadrado(2)
# Saída dos calculos
print(circulo.calculo_area())
print(circulo.calculo_perimetro())
print()
print(quadrado.calculo_area())
print(quadrado.calculo_perimetro())
