class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        goal = 0
        nums = sorted(nums)
        if nums[0] > 0:
            return []
        if nums[-1] < 0:
            return []
        print(nums)
        if len(nums) == 3 and sum(nums) != 0:
            return []
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        for i in range(len(nums) - 1):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] > 0:
                break
            first = nums[i]
            target = goal - first
            left, right = (i + 1), (len(nums) -1)
            print (target, nums[i], nums[left], nums[right])
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    sec = nums[left]
                    third = nums[right]
                    triplet = [first, sec, third]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    left += 1
        return triplets
            
        