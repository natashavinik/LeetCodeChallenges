class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        if target in candidates:
            res.append([target])
            t_i = candidates.index(target)
            print(t_i)
            candidates = candidates[:t_i]
        combo = []
        def dfs(i):
            if i >= len(candidates) or sum(combo) >= target:
                if sum(combo) == target and sorted(combo) not in res:
                    res.append((sorted(combo)).copy())
                return
            combo.append(candidates[i])
            # print("combo append", combo)
            dfs(i)
            combo.pop()
            dfs(i + 1)
        
        for i in range(len(candidates)):
            dfs(i)
            # print("res", res)
        return res
            
                
            