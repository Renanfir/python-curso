n = 234
soma = 0
multiplica = 1
for i in str(n):
    soma += int(i)
    multiplica *= int(i)
print(multiplica-soma)