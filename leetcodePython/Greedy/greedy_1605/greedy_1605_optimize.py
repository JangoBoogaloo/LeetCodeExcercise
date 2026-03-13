class Solution:
    def restoreMatrix(self, rowSum, colSum):
        rows = len(rowSum)
        columns = len(colSum)

        matrix = [[0] * columns for _ in range(rows)]
        row = col = 0
        while row < rows and col < columns:
            matrix[row][col] = min(rowSum[row], colSum[col])
            rowSum[row] -= matrix[row][col]
            colSum[col] -= matrix[row][col]
            # print(f"rowSum[{row}] = {rowSum[row]}, colSum[{col}] = {colSum[col]}")
            if rowSum[row] == 0:
                row += 1
            elif colSum[col] == 0:
                col += 1
        return matrix







