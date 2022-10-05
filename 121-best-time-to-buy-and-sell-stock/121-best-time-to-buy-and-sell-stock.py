class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         stack = [1]
#         prices = [7,1,5,3,6,4]
#         num = 5
        most = 0
        stack = []
        # most = 4
        for num in prices:
            # print(num, stack)
            while stack and num < stack[-1]:
                stack.pop()
            if stack != []:
                most = max(most, num - stack[-1])
            # while stack!= [] and num > stack[-1]:
            #     stack.pop()
            if stack == []:
                stack.append(num)
        
            elif num < stack[-1]:
                stack.append(num)
            # print("end", num, stack, most)
        return most
                
        