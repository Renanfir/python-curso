# 2. Sistema de Notas
# Escreva um programa que recebe as notas de 5 alunos e calcula:

# A média geral da turma.
# O maior e o menor valor das notas.
# Quantos alunos ficaram acima da média.
# Exemplo:

# Entrada: 7.5, 8.0, 6.0, 9.0, 5.5
# Saída:
# Média: 7.2
# Maior: 9.0
# Menor: 5.5
# Acima da média: 3 alunos



import os


qtdAlunos = int(input("Digite a quantidade de alunos: "))
qtdNotas =  int(input("Digite a quantidade de notas: "))
os.system("cls")

alunos = []
notas = []
medias = []

def recolheDados():
    for i in range(qtdAlunos):
        nomeAluno = str(input("digite o nome do "+str(i+1)+"° aluno: "))
        alunos.append(nomeAluno)
        os.system("cls")


        for q in range(qtdNotas):
            nota = float(input("Digite a "+ str(q+1) +"° nota do "+ alunos[i]+": "))
            notas.append(nota)

def calculaMedia():
    for i in range(0, len(notas),2):
        soma = notas[i] + notas[i+1]
        medias.append(soma/qtdNotas)


def verificaMaiorMenor():
    maior = 0
    menor = 10
    for i in notas:
        if i > maior:
            maior = i

        if i <= menor:
            menor = i



def verificaAcimaMedia():
    for i in range(len(medias)):
        if medias[i] < 6:
            print("Aluno "+alunos[i]+" reprovado")
        else:
            print("Aluno "+alunos[i]+" Aprovado")


# print(maior)
# print(menor)
# print(medias)

recolheDados()
calculaMedia()
verificaMaiorMenor()
verificaAcimaMedia()
 
