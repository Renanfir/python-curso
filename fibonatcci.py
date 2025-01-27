numeroDigitado = int(input("Digite um numero: "))


numeros = [0, 1]
if numeroDigitado == 0:
    print("0")
elif numeroDigitado == 1:
    print(0, 1)
else:

    while numeros[-1] < numeroDigitado:
        numeros.append(numeros[-1] + numeros[-2])

    if numeros[-1] != numeroDigitado:
        numeros.pop()

    print(numeros)

# for i in range(numeroDigitado):
#     numeros.append(i)


# 0, 1, 1, 2, 3, 5, 8, 13