class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # s_nums = list(set(nums))
        # print(len(s_nums), len(nums))
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
        