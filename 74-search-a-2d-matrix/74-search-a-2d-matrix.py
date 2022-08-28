class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            p_row = (top + bot) // 2
            if matrix[p_row][-1] < target:
                top = p_row + 1
            elif matrix[p_row][0] > target:
                bot = p_row - 1
            elif matrix[p_row][-1] == target or matrix[p_row][0] == target:
                return True
            else:
                break
        if top > bot:
            return False
        print(matrix[p_row])
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            pivot = (left + right) // 2
            if matrix[p_row][pivot] > target:
                right = pivot - 1
            elif matrix[p_row][pivot] < target:
                left = pivot + 1
            elif matrix[p_row][pivot] == target:
                return True
        return False
                
                
        