class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        n_dict = {}
        for word in strs:
            srt = "".join(sorted(list(word)))
            if srt not in n_dict:
                n_dict[srt] = [word]
            else:
                n_dict[srt].append(word)
        return(n_dict.values())
        