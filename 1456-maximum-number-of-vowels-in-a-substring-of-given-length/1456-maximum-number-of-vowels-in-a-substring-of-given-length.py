class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vow_dict = {"a":0, "e":0, "i":0, "o":0, "u":0}
    
        max_vow = 0
        for i in range(k):
            if s[i] in vow_dict:
                max_vow += 1
        if len(s) == k:
            return max_vow
        curr_vow = max_vow
        
        for i in range(1, len(s) - k + 1):
            j = i + k - 1
            if s[i-1] in vow_dict:
                curr_vow -=1
            if s[j] in vow_dict:
                curr_vow += 1
            max_vow = max(curr_vow, max_vow)
        return max_vow
                
        