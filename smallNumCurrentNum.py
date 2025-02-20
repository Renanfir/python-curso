nums = [8,1,2,2,3]
menores = []
for i in nums:
    count = 0
    for j in nums:
        if j < i:
            count += 1
    menores.append(count)

print(menores)