class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_w = 0
        left, right = 0, len(height) - 1
        
#              x           
#              x   x   x   
#              x   x x x   x
#          x   x   x x x x x
#          x x x   x x x x x
#          x x x x x x x x x
#         [3,2,6,1,5,4,5,3,4]
        
#         l,r = 0,8
#         area = 24
#         14 36
        
        
        while left < right:
            print(left, right)
            width = right - left
            c_height = min(height[left], height[right])
            area = width * c_height
            if area > most_w:
                most_w = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return most_w
            
            
        