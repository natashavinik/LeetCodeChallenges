class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #the maximum amount of times two numbers can add up to k and be removed
        # k = 6
        # nums =  [1,3,3,3,*4,7]
        # goal = 3
        
    
    
    
        
        num_ops = 0
        slow = 0
        
        fast = len(nums)-1
        nums.sort()
        
        while fast > slow:
            if nums[fast] + nums[slow] == k:
                num_ops += 1
                slow += 1
                fast -= 1
            elif nums[fast] + nums[slow] > k:
                fast -= 1
            else:
                slow += 1
            
        
        # for slow in range(len(nums)):
        #     if nums[slow] >= k:
        #         continue
        #     if nums[slow] == "n":
        #         continue
        #     goal = k - (nums[slow])
        #     while fast != slow:
        #         if nums[fast] == goal:
        #             num_ops += 1
        #             nums[fast] = "n"
        #             break
        #         else:
        #             fast -=1 
        #     fast = len(nums)-1
        
        return num_ops
            
                    
            
            
                
        
        