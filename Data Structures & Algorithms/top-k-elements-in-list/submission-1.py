class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            if num not in group:
                group[num] = 1
            else:
                group[num] += 1

        freq_list = [[] for i in range(len(nums) + 1)]
        for num, freq in group.items():
            freq_list[freq].append(num)
        
        ans = []
        for i in range(len(freq_list)-1, 0, -1):
            for n in freq_list[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        # sorted_list = sorted(group.items(), key = lambda x: x[1] , reverse = True)
        # ans = []
        # for i in range(k):
        #     ans.append(sorted_list[i][0])
        # return ans