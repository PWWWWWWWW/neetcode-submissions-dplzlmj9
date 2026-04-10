class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # pseudo
        # brutal sol: hash_map => sorted => first 2
        from collections import defaultdict

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
            
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]
        
        return [item[0] for item in sorted_freq[:k]]    