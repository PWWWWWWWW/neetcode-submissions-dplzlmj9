class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        left = 0
        max_profit = 0

        for right in range(left + 1, len(prices), 1):

            if prices[right] < prices[left]:
                left = right
            else:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)

        return max_profit


