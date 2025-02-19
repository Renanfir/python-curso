points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
minmax = []
for i in range(len(points)):
    minmax.append(points[i][0])

minmax = sorted(minmax)
maior = -10
for i in range(1,len(minmax)):
    if abs(minmax[i-1] - minmax[i]) > maior:
        maior = abs(minmax[i-1] - minmax[i])

print(maior)