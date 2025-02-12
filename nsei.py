n = 2
if n > 2:
     maior = n
else:
    maior = 2
while True:
    if maior % n == 0 and maior % 2 == 0:
        # return maior
        break
    else:
        maior += 1