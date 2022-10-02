class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # stack = [0, 1, ]
        #arr = [0,11,81,94,43,3]
        #res = [0,11, 92, 186, 0]  
        #j = 0, 1, 3
        #i = 0,1, 2 4
        """
        11
        11 + 81
        11 + 81 + 94
        11 + 43 + 43 + 43
        3 + 3 + 3 + 3
        """
        arr = [0] + arr
        stack = [0]
        res = [0] * len(arr)
        
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            res[i] = res[j] + (i-j)*arr[i]
            stack.append(i)
   
      
        return sum(res) % 1000000007
            
            
            
        