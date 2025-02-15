candies = [2,3,5,1,3]
extraCandies = 3
resposta = []
print(max(candies))

for i in candies:
    resposta.append(i + extraCandies >= max(candies))

print(resposta)