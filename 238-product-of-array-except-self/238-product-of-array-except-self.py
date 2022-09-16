class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if 0 in nums:
        #     zero = True
        output = [1 for num in nums]
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        print(output)
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= prefix
            prefix *= nums[i]
        return output
        
#         [1, 2, 3, 4]
        
        
#         [1, 1, 2, 6]
#          *  *  *  *
#         [ 24,  12,  4, 1]
        
#         [ 24,  12,  4 , 1]
                
#         [24, 12, 8, 6]
        
        