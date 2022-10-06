class Solution:
    def climbStairs(self, n: int) -> int:
        # ways = 0 2
#         last = [1, 2]
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
        
#         for num in range(3, n + 1):
#             n_way = last[-1] + last[-2]
#             last.append(n_way)
#         return last[-1]
        num1 = num2 = 1
        for x in range(n-1):
            num1, num2 = num2, num1 + num2
        return num2
#         2 => 2:
#             1 + 1
#             2
        
#         3 => 3:
#             1 + 1 + 1
#             2 + 1
#             1 + 2
            
#         4 => 5: 
#             1 + 1 + 1 + 1
#             1 + 1 + 2
#             1 + 2 + 1
#             2 + 1 + 1
#             2 + 2
       
#     5 => 8:
            
#             1 + 1 + 1 + 1 + 1
#             1 + 1 + 2 + 1
#             1 + 2 + 1 + 1
#             2 + 1 + 1 + 1
#             1 + 1 + 1 + 2
#             2 + 2 + 1
#             2 + 1 + 2
#             1 + 2 + 2
        