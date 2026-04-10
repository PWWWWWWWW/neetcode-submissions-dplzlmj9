class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prev_map:
                return [prev_map[diff], i]

            prev_map[n] = i

        return []












        # hash_num = {}

        # for i in range(len(nums)):
        #     diff = target - nums[i]

        #     if diff in hash_num:
        #         return [hash_num[diff], i]

        #     hash_num[nums[i]] = hash_num.get(nums[i], i)

        # return []