class Solution:
    def climbStairs(self, n: int) -> int:
        stack = [0, 1, 2]
        if n < 3:
            return(stack[n])
        for i in range(3, n+1):
            
            stack.append(stack[-1] + stack[-2])
        return stack[-1]