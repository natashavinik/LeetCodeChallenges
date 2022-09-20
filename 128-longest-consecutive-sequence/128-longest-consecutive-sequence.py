class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for x in nums:
            if x-1 not in nums:
                temp_longest = 0
                while x in nums:
                    temp_longest += 1
                    x += 1
                if temp_longest > longest:
                    longest = temp_longest
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
            
            