class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # h = heights[i] (shorter)
        # w = i(l) - i(r)
        max_con = 0

        for i in range(len(heights)):
            for j in range(len(heights) - 1, i, -1):
                w = j - i

                if heights[i] < heights[j]:
                    h = heights[i]
                else:
                    h = heights[j]

                con = w * h
                max_con = con if con > max_con else max_con

        return max_con
                
