class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #move all 0's to he end of the array, remain order, do in place
        
        
#         nums = [1,0,1]
#                 s f
#         nums = [0,1,0,3,12]
#                   s,  f
#         nums = [1,3,12,0,0]
#                    ,s    f
            
#             #if s == f:
#                 continue
#             # if num[s] == 0 and nums f != 0:
#             num[s], num[f] = num[f], num[s]
#                 s += 1
                
        
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] != 0:
                slow += 1
                continue
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            
        return nums
        
        
#         zeros = 0 
#         for x in nums:
#             if x == 0:
#                 nums.remove(0)
#                 print nums
#                 zeros += 1
#                 print zeros
#             else:
#                 continue
#         print (zeros)
#         while zeros > 0:
#             nums.append(0)
#             zeros -=1
       
#         return nums