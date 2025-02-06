nums = [0,0,0]
resultado = set()

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i != j and i != k and j != k:
                if (nums[i]) + (nums[j]) + (nums[k]) == 0:
                    resultado.add(tuple(sorted([nums[i], nums[j], nums[k]])))
resultado = lista_resultado = list(map(list, resultado))

print(resultado)