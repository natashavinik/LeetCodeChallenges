class Solution:
    def isValid(self, s: str) -> bool:
        open_paren = []
        
        for p in s:
            if p in ['(', '{', '[']:
                open_paren.append(p)
            elif len(open_paren) > 0 and p == ')' and open_paren[-1] == '(':
                open_paren.pop()
            elif len(open_paren) > 0 and p == '}' and open_paren[-1] == '{':
                open_paren.pop()
            elif len(open_paren) > 0 and p == ']' and open_paren[-1] == '[':
                open_paren.pop()
            else:
                return False
        if len(open_paren) > 0:
            return False
        else:
            return True