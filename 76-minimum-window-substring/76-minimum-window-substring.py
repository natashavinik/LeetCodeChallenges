class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(t) > len(s):
            return ""
        t_dict = {}
        for lett in t:
            t_dict[lett] = t_dict.get(lett, 0) + 1
        print(t_dict)
        lett_needs = len(t_dict)
        lett_has = 0
        min_len = float("inf")
        res = ""
        s_dict = {}
        left = 0
        # "abcabdebac"
        # "cda"
        #t_dict = {'c': 1, 'd':1, 'a':1}\
        #lett_needs = 3
        #lett_has = 3
        #min_len = 4
        #res = "abcabd"
        #s_dict = {'a':1, 'c':1, 'd':1}
        #left = 2
        #right = 5
        #r_lett = d
        for right in range(len(s)):
            r_lett = s[right]
            if r_lett not in t_dict:
                continue
            if r_lett in t_dict:
                s_dict[r_lett] = s_dict.get(r_lett, 0) + 1
                if s_dict[r_lett] == t_dict[r_lett]:
                    lett_has += 1
            while lett_has == lett_needs:
                if min_len == float("inf"):
                    min_len = right + 1 - left
                    res = s[left: right + 1]
                else:
                    if right + 1 - left < min_len:
                        min_len = right + 1 - left
                        res = s[left: right + 1]
                if s[left] in t_dict:
                    s_dict[s[left]] -= 1
                    if s_dict[s[left]] < t_dict[s[left]]:
                        lett_has -= 1
                    left += 1
                while left < len(s) and s[left] not in t_dict and left < right:
                    left += 1
                
        return res       
    
                
                
            
            
        