from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._matrixSum = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        self._matrixSum[0][0] = matrix[0][0]
        for row in range(1, len(matrix)):
            self._matrixSum[row][0] = matrix[row][0] + self._matrixSum[row-1][0]
        for col in range(1, len(matrix[0])):
            self._matrixSum[0][col] = matrix[0][col] + self._matrixSum[0][col-1]

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                self._matrixSum[row][col] = (matrix[row][col]
                                             + self._matrixSum[row-1][col] + self._matrixSum[row][col-1]
                                             - self._matrixSum[row-1][col-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            return (self._matrixSum[row2][col2]
                    - self._matrixSum[row1-1][col2] -  self._matrixSum[row2][col1-1]
                    + self._matrixSum[row1-1][col1-1])
        elif row1 > 0:
            return self._matrixSum[row2][col2]  - self._matrixSum[row1-1][col2]
        elif col1 > 0:
            return self._matrixSum[row2][col2] - self._matrixSum[row2][col1-1]
        else:
            return self._matrixSum[row2][col2]






