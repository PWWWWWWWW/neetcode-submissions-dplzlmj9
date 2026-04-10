class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # cal prefix
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # cal suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
        # prod_i = []
        # n = len(nums)

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if j != i:
        #             prod *= nums[j]
        #     prod_i.append(prod)
        
        # return prod_i
