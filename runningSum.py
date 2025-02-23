nums = [1,2,3,4]
resultado = []
for i in range(len(nums)):
    if i == 0:
        resultado.append(nums[i])
    else:
        resultado.append(sum(nums[:i+1:]))

print(resultado)

