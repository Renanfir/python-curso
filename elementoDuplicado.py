nums=[1,1,2,2,5,6,7,8]

contador = 0
contador = contador - len(nums)

for i in nums:
    for j in nums:

        if i == j:
            contador += 1
# if contador == 0:
#     # return False
# else:
#     # return True