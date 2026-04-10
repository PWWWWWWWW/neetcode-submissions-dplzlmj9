class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float("inf")
        max_profit = 0
        
        for price in prices:
            buy_price = price if price < buy_price else buy_price
            current_profit = price - buy_price

            if current_profit > max_profit:
                max_profit = current_profit
        
        return max_profit



