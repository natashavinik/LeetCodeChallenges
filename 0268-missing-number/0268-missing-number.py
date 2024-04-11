class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        n = len(nums) + 1
        
        for i in range(n):
            if i not in num_set:
                return i
#         n = len(nums)
        
#         for i in range(n):
#             print(i)
#             if i in nums:
#                 continue
#             else:
#                 return i
#         return n
    