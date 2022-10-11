from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        w_len = len(word)
        visited = set()
        let_array = []
        for row in board:
            let_array += row
        board_count = Counter(let_array)
        let_count = Counter(word)
        for lett in let_count:
            if let_count[lett] > board_count[lett] or lett not in board_count:
                return False
        """
        [["A","B","C","E"]
         ["S","F","E","S"]
         ["A","D","E","E"]]
        "ABCESEEEFS" """
        
        def dfs(r, c, w_idx, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[w_idx] or (r,c) in visited:
                # if (r,c) in visited:
                #     print((r,c), board[r][c])
                return 0
            if w_idx == w_len - 1:
                # print(word[w_idx])
                # print("Got it!")
                return 1
            visited.add((r,c))
            
            return (dfs(r+1, c, w_idx + 1, visited.copy()) + dfs(r-1, c, w_idx + 1, visited.copy()) + dfs(r, c+1, w_idx + 1, visited.copy()) + dfs(r, c-1, w_idx + 1, visited.copy()))
            
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r, c, 0, visited) >= 1:
                        # print(r,c)
                        return True
        return False
                