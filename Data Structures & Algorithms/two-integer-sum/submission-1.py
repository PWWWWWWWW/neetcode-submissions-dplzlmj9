class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre_num = {}
        
        for i, j in enumerate(nums): 
            dif = target - nums[i]

            if dif in pre_num:
                return [pre_num[dif], i]
            pre_num[j] = i
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]