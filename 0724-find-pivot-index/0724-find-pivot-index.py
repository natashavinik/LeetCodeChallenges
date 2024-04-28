class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_left = 0
        sum_right = sum(nums[1:])
        if sum_left == sum_right:
            return 0
        
        for i in range(1, len(nums)):
            sum_left += nums[i - 1]
            sum_right -= nums[i]
            if sum_left == sum_right:
                return i
        return -1
            