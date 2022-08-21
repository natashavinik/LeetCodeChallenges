class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d_grid = grid
        count = 0
        for i in range(len(d_grid)):
            for j in range(len(d_grid[0])):
                if d_grid[i][j] == "1":
                    self.dfs(d_grid, i, j)
                    count += 1
        return count
                    
                    
    def dfs (self, d_grid, i, j):
        d_grid [i][j] = "0"
        for ar, ac in (1,0), (-1, 0), (0, 1), (0, -1):
            r = i + ar
            c = j + ac
            if 0 <= r < len(d_grid) and 0 <= c < len(d_grid[0]) and d_grid[r][c] == "1":
                self.dfs(d_grid, r, c)
                
                    
        