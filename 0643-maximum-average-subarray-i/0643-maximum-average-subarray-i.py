class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #nums = [1,12,-5,-6,50,3], k = 4
        if len(nums) == 1:
            return nums[0]
        if len(nums) == k:
            return float(sum(nums)) / k
        
        if k == 1:
            return max(nums)
        
        biggest_sum = sum(nums[0:k])
        print(biggest_sum, "initial")
        first_index = 0
        
        i = 0
        j = k - 1
        current_sum = biggest_sum
        
        for i in range(len(nums) - k + 1):
            j = i + k -1
            print(nums[i], nums[j])
            if j == len(nums) - 1:
                break
            current_sum += (nums[j+1] - nums[i])
            if current_sum > biggest_sum:
                biggest_sum = current_sum
                print(biggest_sum)
        print float(51) / 4
        return (float(biggest_sum) / k)
        
    
            
            
        
        
        