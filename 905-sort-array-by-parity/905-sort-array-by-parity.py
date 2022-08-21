class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        e = []
        o = []
        for x in nums:
            if x % 2 == 0:
                e.append(x)
            else:
                o.append(x)
        return e + o