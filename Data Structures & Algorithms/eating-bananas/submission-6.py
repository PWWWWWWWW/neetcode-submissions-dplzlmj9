class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pseudo code
        # iterate
        # pile_time = (pile + speed - 1) // speed
        """
         find the speed ==> min_speed = 1, max_speed = (piles)
         binary search
        """

        min_speed = 1
        max_speed = max(piles)
        res_speed = max_speed

        while min_speed <= max_speed:
            current_speed = min_speed + (max_speed - min_speed) // 2
            time_piles = 0
            
            for pile in piles:
                time_piles += (pile + current_speed - 1) // current_speed

            if time_piles <= h:
                res_speed = current_speed
                max_speed = current_speed - 1
            else:
                min_speed = current_speed + 1

        return res_speed


        







        # if len(piles) == 1:
        #     return piles[0] // h + 1

        # max_speed = max(piles)
        # min_speed = min(piles)

        # for current_speed in range(min_speed, max_speed + 1, 1):
        #     current_hour = 0

        #     for pile in piles:
        #         if pile < current_speed:
        #             pile = 1
        #         else:
        #             pile = (pile + current_speed - 1) // current_speed
        #         current_hour += pile

        #     if current_hour <= h:
        #         return current_speed

        # return -1

        # if not height: return 0
        
        # l, r = 0, len(height) - 1
        # leftMax, rightMax = height[l], height[r]
        # res = 0
        
        # while l < r:
        #     # 誰的牆比較矮，就從哪邊開始算
        #     if leftMax < rightMax:
        #         l += 1
        #         # 更新左邊最高的牆
        #         leftMax = max(leftMax, height[l])
        #         # 水量 = 矮牆 - 柱子高度 (保證不會負數，因為 leftMax 剛更新過)
        #         res += leftMax - height[l]
        #     else:
        #         r -= 1
        #         # 更新右邊最高的牆
        #         rightMax = max(rightMax, height[r])
        #         # 水量 = 矮牆 - 柱子高度
        #         res += rightMax - height[r]
                
        # return res