class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        for x in nums:
            if x-1 not in nums and x + 1 in nums:
                temp_longest = 0
                while x in nums:
                    temp_longest += 1
                    x += 1
                if temp_longest > longest:
                    longest = temp_longest
        if longest == 0:
            return 1
        else:
            return longest
                
                
#         print(start_seq)
#         longest = 0
#         for x in start_seq:
#             if x + 1 not in nums:
#                 continue
#             temp_longest = 0
#             y = x
#             while y in nums:
#                 temp_longest += 1
#                 y += 1
#             longest = max(longest, temp_longest)
#         return longest
            
            