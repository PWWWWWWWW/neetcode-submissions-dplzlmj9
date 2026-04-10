class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # constraints: len(n + 1), element:[1, n]
        # purpose: find dupli, with others all appears one time
        
        # pseudo
        # [1, 3, 8, 3, 2]
        # optimal sol => [1 -> 3 -> 8 -> 3 -> 2]
        # find meet: two pointers fast slow
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                new_slow = slow
                break

        # distance(meet -> target) = distance(start -> target)
        ptr1 = 0
        ptr2 = new_slow
        
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1



        # # brute force sol => time complexity: O(n), space complexity: O(n)
        # from collections import defaultdict

        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1

        # for num, freq in count.items():
        #     if freq > 1:
        #         return num

        # return 0
        