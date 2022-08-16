class Solution:
    def isPalindrome(self, s: str) -> bool:
        n_str = ""
        for char in s:
            if char.isalnum():
                n_str += char.lower()
        print(n_str)
        if n_str == n_str[::-1]:
            return True
        else:
            return False