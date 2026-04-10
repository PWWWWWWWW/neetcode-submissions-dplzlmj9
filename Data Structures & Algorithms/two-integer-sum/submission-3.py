class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict()

        for left in range(len(nums)):
            diff = target - nums[left]

            if diff in hash_map:
                return [hash_map[diff], left]

            hash_map[nums[left]] = left

        return []