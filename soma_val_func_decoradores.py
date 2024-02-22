#Criando função decoradora
def cria_funcao(funcao):
    def interna(*args, **kwargs):
        print("Iniciando")
        val_total = funcao(*args, **kwargs)
        return val_total
    return interna

# Decoradora criando função
@cria_funcao
def f1(x, y):
    print("O valor de x é de", x)
    print("O valor de y é de", y)
    return x + y

# Utilizando a função f1 para somar dois numeros
f1 = f1(1, 2)
print("O valor total é de:",f1)