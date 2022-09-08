class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        
        for right in range(l, len(prices)):
            if prices[right] < prices[l]:
                l = right
            profit = max(profit, prices[right] - prices[l])
        return profit
            
#         if prices == sorted(prices):
#             return (prices[-1] - prices[0])
#         s_prices = sorted(prices)
#         if prices == s_prices[::-1]:
#             return 0
        
        
#         profit = 0
        
#         for i in range(len(prices) - 1):
#             if i != 0 and prices[i] <= prices[i - 1]:
#                 continue
#             rest = prices[i+1:]
#             print(i, rest)
#             m_rest = max(rest)
#             if prices[i] >= max(rest):
#                 continue
#             if prices[i] < m_rest:
#                 profit = max(profit, max(prices[i+1:]) - prices[i])
#         return profit
                
        