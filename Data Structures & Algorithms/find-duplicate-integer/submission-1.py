class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # constraints: len(n + 1), element:[1, n]
        # purpose: find dupli, with others all appears one time
        
        # pseudo
        # [1, 3, 8, 3, 2]
        # brute force sol
        from collections import defaultdict

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            if freq > 1:
                return num

        return 0
        