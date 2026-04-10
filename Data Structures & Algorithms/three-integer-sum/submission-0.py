class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        else:
            ans = []
            for combo in combinations(nums, 3):
                if sum(combo) == 0:
                    is_duplicate = False
                    for i in ans:
                        if sorted(i) == sorted(combo):
                            is_duplicate = True
                            break

                    if not is_duplicate:
                        ans.append(combo)
        return ans

        # distinct_num = set(nums)
        # if len(distinct_num) < 3:
        #     return []
        # else:
        #     ans = []
        #     for combo in combinations(distinct_num, 3):
        #         if sum(combo) == 0:
        #             ans.append(combo)
        # return ans
                