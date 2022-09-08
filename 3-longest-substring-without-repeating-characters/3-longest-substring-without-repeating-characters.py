class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, l_len = 0, 0
        lett_set = []
        
        for right in range(len(s)):
            while s[right] in lett_set:
                lett_set.pop(0)
                left += 1
            lett_set.append(s[right])
            l_len = max(l_len, len(lett_set))
        return l_len
            
        
        