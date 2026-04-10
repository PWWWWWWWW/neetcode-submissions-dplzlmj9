class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hash_num:
                return [hash_num[diff], i]

            hash_num[nums[i]] = hash_num.get(nums[i], i)

        return []