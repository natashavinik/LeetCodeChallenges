class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        [4,-2,-3,4,1]
        
        6
        7 + 1
        7 + 7 + 7 35 
        7 + 7 + 7 + 3 = 59
        
        21, -21
        4
        -2, -2
        -3, -3, -3
        -3, -3, -3, 4
        -3, -3, -3, 1, 1
        
        0
        0, 4
        -2, -2, -2,
        
        
        6, 7, 7, 7, 7, 7, 7, 7, 3
        
        
        4
        4, -2
        4, -2, -3
        4, 4, 4, 4
        4, 4, 4, 4, 1 = 38"""
        
        # [1, 2, 3]
        # [0]
        #[0, 0, 0]
        # i = 0
        # j = 0
        onums = nums
        s_stack = []
        min_res = [0] * len(onums)
        for i in range(len(onums)):
            print(i)
            while s_stack and onums[s_stack[-1]] > onums[i]:
                s_stack.pop()
            if s_stack == []:
                j = -1
            else:
                j = s_stack[-1]
            min_res[i] = min_res[j] + (i-j) * onums[i]
            s_stack.append(i)
        print(sum(min_res))
        
#         [1,2,3]
#         b_stack = [1]
#         [1, 4, 9]
#         i= 0,1, 2
#         j= -1
        b_stack = []
        max_res = [0] * len(onums)
        for i in range(len(onums)):
            # print(i, max_res)
            while b_stack and onums[b_stack[-1]] < onums[i]:
                b_stack.pop()
            if b_stack == []:
                j = -1
            else:
                j = b_stack[-1]
            max_res[i] = max_res[j] + (i - j) * onums[i]
            b_stack.append(i)
        print(sum(max_res))
        
        return (sum(max_res) - sum(min_res))
        
        