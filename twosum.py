numbers=[2,3,4]
target=6
resposta = []
for i in numbers:
    for j in numbers:
        if i != j:
            if i + j == target and len(resposta)<2:
                resposta.append(numbers.index(i)+1)
                resposta.append(numbers.index(j)+1)

print(resposta)