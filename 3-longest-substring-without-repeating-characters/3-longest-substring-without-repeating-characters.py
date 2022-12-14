class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start, longest_sub = 0, 0 #1, 2, 3
        letters = {} #{a:3, b:1, c:2}
        for window_end in range(len(s)):
            right = s[window_end]
            print(s[window_end])
            if right in letters:
                window_start = max(window_start, letters[right] + 1)
                # (1)
            letters[right] = window_end
            longest_sub = max(window_end - window_start + 1, longest_sub)
        return longest_sub
        
        