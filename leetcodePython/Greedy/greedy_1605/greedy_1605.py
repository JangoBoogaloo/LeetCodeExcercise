class Solution:
    def restoreMatrix(self, rowSum, colSum):
        rows = len(rowSum)
        columns = len(colSum)

        currRowSum = [0] * rows
        currColSum = [0] * columns

        matrix = [[0] * columns for _ in range(rows)]
        for row in range(rows):
            for col in range(columns):
                rowRemain = rowSum[row] - currRowSum[row]
                colRemain = colSum[col] - currColSum[col]
                matrix[row][col] = min(rowRemain, colRemain)
                currRowSum[row] += matrix[row][col]
                currColSum[col] += matrix[row][col]
        return matrix








