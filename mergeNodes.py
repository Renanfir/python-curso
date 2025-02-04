head = [0,3,1,0,4,5,2,0]
soma = 0

grupo = []
for i in head:
    if i == 0:
        if soma != 0:
            grupo.append(soma)
        soma = 0
    else:
        soma += i


#não funcionou, estudar ListNode