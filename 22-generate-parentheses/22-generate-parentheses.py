class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        # if n_open < n_closed, we can add n closed
        # if n_opn < n, we can add n
        def backtrack(n_open, n_closed):
            if n_open == n_closed == n:
                res.append("".join(stack))
                return
              
            if n_open > n_closed:
                stack.append(")")
                backtrack(n_open, n_closed + 1)
                stack.pop()
                
            if n_open < n:
                stack.append("(")
                backtrack(n_open + 1, n_closed)
                stack.pop()
                
          
        backtrack(0, 0)
        return res
        
        
        