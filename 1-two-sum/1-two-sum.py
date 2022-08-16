class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        
        for i in range(len(nums)):
            onum = target - nums[i]
            if onum in new_dict:
                return (new_dict[onum], i)
            new_dict[nums[i]] = i
    
        