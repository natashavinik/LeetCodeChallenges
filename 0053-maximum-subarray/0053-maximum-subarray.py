class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        curr_sum = 0
        
        # [-2,1,-3,4,-1,2,1,-5,4]
        #                      x
        # max = 6
        # curr_sum = 5
        
        
        for num in nums:
            if curr_sum < 0 and curr_sum < num:
                curr_sum = 0
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
        return max_sum