import collections

nums = [3,1,10,2,4,8,3,2,9,5,4,8,4,3,1,5,5,7,2,2,8,8,10,1,7,10,5,10,2,9,8,7,10,3,10,10,9,8,10,7,3,10,2,9,8,3,1,2,1,6,4,9,7,5,6,7,4,5,3,1,4,2,2,1,10,4,2,7,3,6,5,7,3,10]
n = {}
for i in nums:
    if not i in n:
        n[i] = []
    n[i].append(i)

output = 0
for i in range(11):
    if i not in n:
        continue
    else:
        output += (len(n.get(i)) * (len(n.get(i)) - 1)) / 2


print(int(output))
