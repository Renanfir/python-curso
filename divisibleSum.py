n = 10 
m = 3
divi = []
Ndivi = []

for i in range(1, n+1):
    if i % m == 0:
        divi.append(i)
    else:
        Ndivi.append(i)

print(sum(Ndivi) - sum(divi))