height = [1,7,2,5,4,7,3,6]
ordened_height = sorted(height)
resultado = 0

for i in range(len(ordened_height)):
    for j in range(i+1, len(ordened_height)):
        resultado = max(resultado, height[i], height[j] * (j - i))

print(resultado)
    