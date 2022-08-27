class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
        char_dict = {}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        for lett in t:
            if lett not in char_dict:
                return False
            if lett in char_dict and char_dict[lett] > 0:
                char_dict[lett] -= 1
                if char_dict[lett] == 0:
                    char_dict.pop(lett)
            else:
                return False
        if char_dict == {}:
            return True
            
        