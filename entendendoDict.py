gruposEspalhados = ["abc1","abc2","abc3","cde1","cde3","fgh2","fgh4"]

gruposReunidos = {}

for i in gruposEspalhados:
    if i[0:3] not in gruposReunidos:
        gruposReunidos[i[0:3]] = []
    gruposReunidos[i[0:3]].append(i)

print(gruposReunidos)

#Essa foi de first