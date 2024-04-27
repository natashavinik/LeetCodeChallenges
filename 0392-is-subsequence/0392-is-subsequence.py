class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #if s is a subsequence of t, return true
        #otherwise return false
        
        # slow_lim = len(s) - 1
        # st = s
        
       # s= "abc"
       #t = "ahbgdc"
        
        #s_in = 2
        #slow = 4
        #fast = 5
        
        s_in = 0
        
        slow = 0
        fast = len(t) - 1
        if s == "":
            return True
        if s == t:
            return True
        
        while slow <= fast:
            if t[slow] == s[s_in]:
                s_in += 1
                if s_in == len(s):
                    return True
            slow += 1
            
        return False