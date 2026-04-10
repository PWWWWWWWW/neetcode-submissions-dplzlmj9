class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 直接初始化最低價為第一天，獲利為 0
        # 這樣連長度小於 2 的判斷都省了，程式碼更乾淨
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # 1. 看看今天是不是比歷史最低點還低
            if price < min_price:
                min_price = price
            # 2. 如果今天賣掉賺得比紀錄多，就更新紀錄
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) < 2:
#             return 0
        
#         left = 0
#         max_profit = 0

#         for right in range(left + 1, len(prices), 1):

#             if prices[right] < prices[left]:
#                 left = right
#             else:
#                 current_profit = prices[right] - prices[left]
#                 max_profit = max(max_profit, current_profit)

#         return max_profit


