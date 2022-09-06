class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        if target in candidates:
            res.append([target])
            t_i = candidates.index(target)
            print(t_i)
            candidates = candidates[:t_i]
        print("candidates", candidates)
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
        dfs(0, [], 0)
        return res
            
                
            