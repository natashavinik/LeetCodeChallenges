class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if len(t) > len(s):
            return ""
        
        r_len = float("infinity")
        res = []
        t_dict = {}
        for lett in t:
            t_dict[lett] = t_dict.get(lett, 0) + 1
        print(t_dict)
        l = 0
        have, need = 0, len(t_dict)
        n_dict = {}
        for r in range(len(s)):
            if s[r] in t_dict:
                n_dict[s[r]] = n_dict.get(s[r], 0) + 1
                if t_dict[s[r]] == n_dict[s[r]]:
                    have += 1
            while have == need:
                if r - l + 1 < r_len:
                    r_len = r - l + 1
                    res = [l,r]
                if s[l] in n_dict:
                    n_dict[s[l]] -= 1
                    if n_dict[s[l]] < t_dict[s[l]]:
                        have -= 1
                l += 1
        if res == []:
            return ""
        return (s[res[0]:res[1] + 1])
                        
                            
                            
        
                
            
            
            
        