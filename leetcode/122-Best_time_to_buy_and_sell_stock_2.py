# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 2147483647
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

#         new = []
#         for i in range(1, len(prices)):
#             if prices[i-1] < prices[i]:
#                 buy = prices[i-1]
#                 new.append(buy)
#         if len(new) == 0:
#             return 0
#         else:
#             buy = min(new)
#             place = prices.index(buy)
#             prices = prices[place+1:]
#             sell = max(prices)

#             profit = sell - buy
#             return profit
