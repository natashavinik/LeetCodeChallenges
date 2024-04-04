class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_dict = {}
        for num in nums:
            if num not in new_dict:
                new_dict[num] = 1
            else:
                new_dict.pop(num)
        for x in new_dict:
            return x
            
                
        