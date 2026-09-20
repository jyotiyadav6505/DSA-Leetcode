class Solution(object):

    def rotate(self, matrix):

        n = len(matrix)

        # Transpose the matrix
        for i in range(0, n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse every row
        for i in range(0, n):
            matrix[i].reverse()

