class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            n_left = numbers[left]
            n_right = numbers[right]
            n_sum = n_left + n_right
            if n_sum == target:
                return [left + 1, right + 1]
            elif n_sum < target:
                left += 1
            else:
                right -= 1
                    
        
        
        
        # right = 0
        # prevnum = numbers[0] - 1
        # for left in range(len(numbers)):
        #     if numbers[left] == prevnum:
        #         continue
        #     right = left + 1
        #     if numbers[left] + numbers[-1] < target:
        #         continue
        #     rest = target - numbers[left]
        #     while right < len(numbers) and numbers[right] <= rest:
        #         if numbers[right] == rest:
        #             return [left + 1, right + 1]
        #         right += 1
        #     prevnum == numbers[left]
