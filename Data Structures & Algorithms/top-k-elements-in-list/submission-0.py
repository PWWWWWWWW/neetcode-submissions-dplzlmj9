class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            if num not in group:
                group[num] = 1
            else:
                group[num] += 1

        sorted_list = sorted(group.items(), key = lambda x: x[1] , reverse = True)
        ans = []
        for i in range(k):
            ans.append(sorted_list[i][0])
        return ans