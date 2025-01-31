nums = [1,2,2,3,3,3]
k = 2
grupos = {}
for i in nums:
    if i not in grupos:
        grupos[i] = []
    grupos[i].append(i)

grupos = sorted(grupos.items(), key=lambda x: len(x[1]), reverse=True)#by GPT


output = []

for j in range(k):
    output.append(grupos[j][0])

print(output.sort())

#essa foi radicori +40 min pra fazer



