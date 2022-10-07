class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        print(abs(3-4))
        while left < right:

            m_height = min(height[left], height[right])
            water = m_height * (right - left)
            print(water, left, right)
            if water > res:
                res = water
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
            
        return res