class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            l_s = str(len(s))
            ns = l_s + "#" + s
            res += ns
        print(res)
        return res
            
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        left,right = 0,0
        # 13#BmI3FS~J9#vmk1#h
        while left < len(s):
            while s[right] != "#":
                right += 1
            len_s = int(s[left:right]) #len_s = 2
            left = right + 1#l,r = 2,2
            right= left + len_s #l,r = 2,4
            res.append(s[left:right])
            left = right
        return res
            
            
            
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))