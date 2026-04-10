class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_set = set()
        for num in nums:
            if num in distinct_set:
                return True
            distinct_set.add(num)
        return False
        # distinct_list = []
        # for i in range(len(nums)):
        #     if nums[i] not in distinct_list:
        #         distinct_list.append(nums[i])
        #     else:
        #         return True
        # return False