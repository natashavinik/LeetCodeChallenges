class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if max(nums) < 0:
            return max(nums)
        # stack = []
        max_sum = 0
        current_sum = 0
        
        for x in nums:
            current_sum = max(0, current_sum + x)
            max_sum = max(current_sum, max_sum)
        return max_sum
        
#         for i in range(len(nums)):
#             if i == 0:
#                 stack.append(nums[i])
#                 continue
#             if stack[-1] < 0 and stack[-1] < nums[i]:
#                 stack.pop()
#                 stack.append(nums[i])
#                 max_sum = max(stack[-1], max_sum)
#             else:
#                 stack.append(stack[-1] + nums[i])
#                 max_sum = max(stack[-1], max_sum)
#             print(i, stack)
#         return max_sum
        
        
        