accounts = [[2,8,7],[7,1,3],[1,9,5]]
big = -101
for i in accounts:
    if sum(i) > big:
        big = sum(i)

print(big)