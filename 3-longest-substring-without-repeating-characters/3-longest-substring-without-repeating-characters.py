class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_len = 0
        left = 0
        charset = set()
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            if len(charset) > l_len:
                l_len = len(charset)
        return l_len
            
        