numeroDigitado = str(input("Digite um numero: "))
numeroInvertido = numeroDigitado[::-1]
print(numeroInvertido)

if numeroInvertido == numeroDigitado:
    print("Este número é um palindromo")
else:
    print("Não é palindromo")