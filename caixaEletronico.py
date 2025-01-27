notas = [100, 50, 20, 10, 5, 2]
valor = int(input("Digite o valor: "))
qtd = []
resultado = {}

for nota in notas:
    if valor >= nota:
        qtd = valor // nota
        resultado[nota] = qtd
        valor %= nota

for nota, quantidade in resultado.items():
    print(f"{quantidade} nota(s) de R${nota}")


