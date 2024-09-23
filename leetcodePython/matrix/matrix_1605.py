from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        curr_row_sum = [0] * rows
        curr_col_sum = [0] * cols

        matrix = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                curr_r = rowSum[row] - curr_row_sum[row]
                curr_c = colSum[col] - curr_col_sum[col]
                curr = min(curr_r, curr_c)
                matrix[row][col] = curr
                curr_row_sum[row] += matrix[row][col]
                curr_col_sum[col] += matrix[row][col]
        return matrix


class SolutionOptimize:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        matrix = [[0] * cols for _ in range(rows)]
        row, col = 0, 0
        while row < rows and col < cols:
            matrix[row][col] = min(rowSum[row], colSum[col])
            rowSum[row] -= matrix[row][col]
            colSum[col] -= matrix[row][col]

            # one of them will be bigger than 0, for the smaller than 0 data, move forward
            if rowSum[row] == 0:
                row += 1
            else:
                col += 1
        return matrix
