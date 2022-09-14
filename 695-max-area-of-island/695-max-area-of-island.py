class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        rows = len(grid)
        cols = len(grid[0])
        temp_area = 0
        d_grid = grid
        visit = set()

        def dfs(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visit or d_grid[r][c] == 0:
                return 0
            visit.add((r,c))
            
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c-1))
        
        for r in range(rows):
            for c in range(cols):
                if d_grid[r][c] == 1 and(r,c) not in visit:
                    maxarea = max(maxarea, dfs(r,c))
        return maxarea
                