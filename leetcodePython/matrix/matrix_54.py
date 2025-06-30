from typing import List


class Solution:
    _DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    _INVALID = -101
    def _isValid(self, row, col, matrix: List[List[int]]) -> bool:
        if row < 0 or row > len(matrix) - 1:
            return False
        if col < 0 or col > len(matrix[0]) - 1:
            return False
        if matrix[row][col] == self._INVALID:
            return False
        return True

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directionIndex = 0
        result = [matrix[0][0]]
        row, col = 0, 0
        matrix[row][col] = self._INVALID
        while len(result) < len(matrix) * len(matrix[0]):
            newRow = row + self._DIRECTIONS[directionIndex][0]
            newCol = col + self._DIRECTIONS[directionIndex][1]
            if not self._isValid(newRow, newCol, matrix):
                directionIndex = (directionIndex + 1) % len(self._DIRECTIONS)
                continue
            result.append(matrix[newRow][newCol])
            matrix[newRow][newCol] = self._INVALID
            row, col = newRow, newCol
        return result






