class Solution(object):
    def shuffle(self, nums, n):
        resposta = []
        for i in range(n, len(nums)):
            resposta.append(nums[i-(n)])
            resposta.append(nums[i])
            

        return resposta