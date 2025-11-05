class Solution:
    def restoreMatrix(self, rowSum, colSum):
        rows = len(rowSum)
        columns = len(colSum)

        matrix = [[0] * columns for _ in range(rows)]
        for row in range(rows):
            for col in range(columns):
                matrix[row][col] = min(rowSum[row], colSum[col])
                rowSum[row] -= matrix[row][col]
                colSum[col] -= matrix[row][col]
        return matrix








