class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}
        
        for i in range(len(nums)):
            need = target - nums[i]
            if need in n_dict:
                return (n_dict[need], i)
            n_dict[nums[i]] = i
        
        