class Solution:
    def rob(self, nums: List[int]) -> int:
        steal_1 = 0
        steal_2 = 0
        # [1,2,3,1]
        # n = 1
        # temp = 3
        # steal_1 = 4
        # steal_2 = 3
        # steal_1, steal_2, n, n+ 1, n+2
        for n in nums:
            temp = max(steal_1 + n, steal_2)
            steal_1 = steal_2
            steal_2 = temp
            # print(steal_1, steal_2)
            
        return steal_2
        
#         for i in range(0,len(nums), 2):
#             steal_1 += nums[i]
            
#         for i in range(1,len(nums), 2):
#             steal_2 += nums[i]
#         return max(steal_1, steal_2)
        