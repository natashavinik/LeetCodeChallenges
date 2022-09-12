class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letset = []
        l_len = 0
        left = 0
        for right in range(len(s)):
            while s[right] in letset:
                letset.pop(0)
                left += 1
            letset.append(s[right])
            l_len = max(l_len, len(letset))  
        return l_len
