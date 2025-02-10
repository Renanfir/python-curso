head = [18,6,10,3]

grupo = []

for a, b in zip(head[::2], head[1::2]):
    i = 1
    while True:
        if i % a == 0 and i % b == 0:
            grupo.append(a)
            grupo.append(i)
            grupo.append(b)
            break
        i += 1
    
print(grupo)