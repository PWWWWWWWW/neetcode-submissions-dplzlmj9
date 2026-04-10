class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if not nums:
            return -1
        
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return -1



        # for i in range(len(nums)):
        #     end = (l + r) / 2
        #     if end != i:
        #         if nums[i] < target:
        #             i = (i + r)/2
        #             r = i
        #         elif nums[i] > target:
        #             i = (i + l)/2
        #             l = i
        #         else:
        #             return i
        #     else:
        #         break
     
        # return -1