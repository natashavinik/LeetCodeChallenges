class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        l_dict = {}
        left = 0
        
        for right in range(len(s)):
            l_dict[s[right]] = l_dict.get(s[right], 0) + 1
            
            while (right - left + 1) - max(l_dict.values()) > k:
                l_dict[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
    
        return res
            
                
                
                
                
                
        #     if s[right] in l_dict:
        #         l_dict[s[right]] += 1
        #         res = max(res, l_dict[s[right]])
        #     else:
        #         l_dict = {}
        #         l_dict[s[right]] = 1
        # return res
                
            
            