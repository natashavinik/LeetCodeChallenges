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
            elif height[right] < height[left]:
                right -= 1
            else:
                if height[left + 1] > height[right -1]:
                    left += 1
                elif height[left + 1] < height[right -1]:
                    right -= 1
                else:
                    left += 1
                
        return most_w
            
            
        