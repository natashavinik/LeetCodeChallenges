class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         stack = [1]
#         prices = [7,1,5,3,6,4]
#         num = 5
#         most = 0
#         stack = []
#         for num in prices:
#             while stack and num < stack[-1]:
#                 stack.pop()
#             if stack != []:
#                 most = max(most, num - stack[-1])
#             if stack == []:
#                 stack.append(num)
        
#             elif num < stack[-1]:
#                 stack.append(num)
#         return most
        profit = 0
        l = 0
        
        for right in range(l, len(prices)):
            if prices[right] < prices[l]:
                l = right
            profit = max(profit, prices[right] - prices[l])
        return profit
                
        