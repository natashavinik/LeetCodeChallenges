class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # n_matrix = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
        # print(n_matrix, matrix)
        # for i in range(len(matrix)):
        #     print(n_matrix)
        #     for j in range(len(matrix[0])):
        #         n_matrix[j][i] = matrix[i][j]
        # return n_matrix
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
            