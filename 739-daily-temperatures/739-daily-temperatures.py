class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_i, stack_t = stack.pop()
                answer[stack_i] = i - stack_i
            stack.append([i,t])
            # print("stack", stack, "answer", answer)
        return answer
            
            
        
        
        
        
        
        
#         for i in range(len(temperatures)-1):
#             if temperatures[i+1] > temperatures[i]:
#                 answer.append(1)
#             else:
#                 next_n = i+1
#                 n_num = 0
#                 while next_n < len(temperatures) and temperatures[next_n] <= temperatures[i]:
#                     next_n += 1
#                     n_num += 1
#                 answer.append(n_num + 1)
                
#         answer.append(0)
#         return answer
                
                
        