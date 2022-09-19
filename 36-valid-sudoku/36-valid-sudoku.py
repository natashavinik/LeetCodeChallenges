class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c_dict = {}
        #below for rows
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] not in c_dict:
                        c_dict[board[r][c]] = 1
                    else:
                        return False
            c_dict = {}
        #below for cols
        c_dict = {}
        for c in range(9):
            for r in range(9):
                if board[r][c] != ".":
                    if board[r][c] not in c_dict:
                        c_dict[board[r][c]] = 1
                    else:
                        return False
            c_dict = {}
        c_dict = {}

        for br in (0, 3, 6):
            for bc in (0, 3, 6):
                for cr in range(3):
                    for cc in range(3):
                        r = br + cr
                        c = bc + cc
                        # print("br|bc|cr|cc|r|c")
                        # print(br, bc, cr, cc, r,c)
                        if board[r][c] != ".":
                            if board[r][c] not in c_dict:
                                c_dict[board[r][c]] = 1
                            else:
                                return False
                c_dict = {}
                
        return True
    
#     [[".",".","."|,".","5","."|".","1","."],
#      [".","4","."|"3",".","."|".",".","."],
#      [".",".","."|".",".","3"|".",".","1"],
#      -------------------------------------
#      ["8",".","."|".",".","."|".","2","."],
#      [".",".","2"|".","7","."|".",".","."],
#      [".","1","5"|".",".","."|".",".","."],
#      -------------------------------------
#      [".",".","."|".",".","2"|".",".","."],
#      [".","2","."|"9",".","."|".",".","."],
#      [".",".","4"|".",".","."|".",".","."]]