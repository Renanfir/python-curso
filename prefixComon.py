import numpy as np
a = [1,3,2,4]
b = [3,1,2,4]
count = 0
resposta = []
for i in range(1,len(a)+1):
    count = 0
    temp1 = []
    temp2 = []
    temp1 = sorted(a[:i])
    temp2 = sorted(b[:i])
    for j in range(len(temp1)):
        if temp1[j] == temp2[j]:
            count += 1
    resposta.append(count)
            

print(resposta)




