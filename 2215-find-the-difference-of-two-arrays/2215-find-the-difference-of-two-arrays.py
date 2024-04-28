class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans_0 = []
        ans_1 = []
        num1_dict = dict.fromkeys(nums1, 0)
        num2_dict = dict.fromkeys(nums2, 0)
        
        for num in nums1:
            if num not in num2_dict:
                if num not in ans_0:
                    ans_0.append(num)
        
        for num in nums2:
            if num not in num1_dict:
                if num not in ans_1:
                    ans_1.append(num)
                    
        return [ans_0, ans_1]