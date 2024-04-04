class Solution(object):
    def twoSum(self, nums, target):
        #return indices that add up to target
        # for i,num in nums:
        #     if target - num in nums:
        newdict = {}

        for i in range(len(nums)):
            o_num = target - nums[i]
            if o_num in newdict:
                return [newdict[o_num], i]
            newdict[nums[i]] = i    
      

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        