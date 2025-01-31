nums = [0, -1]
nums = sorted(nums)

if len(set(nums)) == 1:
    print("1")
else:
    maior = 1
    gp = []

    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i + 1]:
            maior += 1
        else:
            gp.append(maior)
            maior = 1
    gp.append(maior)

    if len(nums) > 2:
        tamanho = len(gp) - 1
        gp = sorted(gp)
        print(gp[tamanho] + 1)
    elif len(nums) ==2:
        tamanho = len(gp) - 1
        gp = sorted(gp)
        print(gp[tamanho])
    
    else:
        print("0")





