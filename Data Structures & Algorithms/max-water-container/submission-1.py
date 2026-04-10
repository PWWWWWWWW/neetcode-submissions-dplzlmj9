class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_con = 0
        
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])

            current_area = w * h
            max_con = max(current_area, max_con)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_con

        # max_con = 0

        # for i in range(len(heights)):
        #     for j in range(len(heights) - 1, i, -1):
        #         w = j - i

        #         if heights[i] < heights[j]:
        #             h = heights[i]
        #         else:
        #             h = heights[j]

        #         con = w * h
        #         max_con = con if con > max_con else max_con

        # return max_con
                
