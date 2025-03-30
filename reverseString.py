palavra = "Abacaxizes"
a = []
revertido = ""

for i in range(1,len(palavra)+1):
    a.append(palavra[-i])


for char in a:
    revertido = revertido + char 

print(revertido)