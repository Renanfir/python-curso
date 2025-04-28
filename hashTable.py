#Estrutura inicial hash table
class HashTable:
    def __init__(self, size):
        self.data = [None] * size


    #Para cada caractere(char) da palavra é pego o codigo unicode (ord())
    #Multiplica palo indice ( i ) Soma isso tudo para formar um valor grande
    #E depois é feito o resto da divisão( % ) pelo tamanho da lista( len(self.data) )
    #que vai gerar um numero que caiba dentro da lista
    def _hash(self, key):
        hash_value = 0
        for i, char in enumerate(key):
            hash_value = (hash_value + ord(char) * 1) % len (self.data)
        return hash_value


    #Primeiro é calculado o adress( self._hash(key) )
    #depois é verificado se há espaço nesse adress, caso sim
    #é adicionado na lista (self.data) no endereço (adress) a chave e valor (key, value)
    #e é reornado a lista
    def set(self, key, value):
        adress = self._hash(key)
        if not self.data[adress]:
            self.data[adress] = []
        self.data[adress].append([key, value])
        return self.data

    #Primeiro é calculado o adress( self._hash(key) )
    #depois é pego o current_bucket com as chaves e valores que nele estão
    #se existir algo, é percorrido um looping e caso a chave( pair[0]) for encontrada
    # é retornado o value( pair[1]).
    def get(self, key):
        adress = self._hash(key)
        current_bucket = self.data[adress]
        if current_bucket:
            for pair in current_bucket:
                if pair[0] == key:
                    return pair[1]
        return None
    
myHashTable = HashTable(50)
myHashTable.set('grapes', 10)
myHashTable.set('oranges', 5)
print(myHashTable.get('grapes'))