frase = "zaz"
alfabeto = [chr(letra) for letra in range(97, 123)]
valores = []
resultados = []
for i in frase:
    for j in alfabeto:
        if i == j:
            valores.append(alfabeto.index(j)+97)


for i in range(len(valores)-1):
    resultados.append(abs(valores[i] - (valores[i + 1])))

print(sum(resultados))




