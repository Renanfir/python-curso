def cria_funcao(funcao):
    def interna(*args, **kwargs):
        print("Iniciando")
        val_total = funcao(*args,**kwargs)
        return val_total
    return interna


@cria_funcao
def f1(x, y):
    print("O valor de x é de",x)
    print("O valor de y é de",y)
    return x + y

f1 = f1(1,2)
print("O valor total é de:",f1)