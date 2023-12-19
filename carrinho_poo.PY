class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
    
    def listar(self):
        for p in self._produtos:
            print(p.nome, p.preco)
        


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()

p1 = Produto('iogurte',9)
p2 = Produto('salgadinho',3)

carrinho.inserir(p1,p2)
carrinho.listar()











