class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        max_p = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            
            else:
                profit = prices[right] - prices[left]
                max_p = max(max_p, profit)

        return max_p