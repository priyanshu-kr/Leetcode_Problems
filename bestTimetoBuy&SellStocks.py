from typing import List

prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self, prices:List[int]) -> int:
        lowest = float('inf')     # whatever the first price is, it becomes the lowest.
        max_profit = 0

        for price in prices:
            # if price <= lowest:
            #     lowest = price
            lowest = min(lowest, price)
            
            profit = price - lowest
            
            max_profit = max(profit, max_profit)
            # if profit >= max_profit:
            #     max_profit = profit
        
        return max_profit

sol = Solution()
print(sol.maxProfit(prices))