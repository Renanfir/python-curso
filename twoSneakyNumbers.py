nums = [0,1,1,0]

grupo = {}
resposta = []

for i in nums:
    if i not in grupo:
        grupo[i] = []
    grupo [i].append(i)

for i in grupo.values():
    if len(i) == 2:
        resposta.append(i[0])

print(resposta)