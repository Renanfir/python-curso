nums = [2,1,3,5,6]
k = 5
multiplier = 2
t = 0
for i in range(k):
    menor = min(nums)
    nums[nums.index(menor)] = menor * multiplier

print(nums)