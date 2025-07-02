from typing import List


class Solution:
    _DATASET = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    _EMPTY = "."

    @staticmethod
    def _boxOf(row, col) -> int:
        boxCol = col // 3
        boxRow = row // 3

        return boxRow * 3 + boxCol

    @staticmethod
    def _isValid(data:str, dataSet:set) -> bool:
        if data not in dataSet:
            return False
        dataSet.remove(data)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numForRow = [set(self._DATASET) for _ in range(9)]
        numForCol = [set(self._DATASET) for _ in range(9)]
        numForBox = [set(self._DATASET) for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board)):
                data = board[row][col]
                if data == self._EMPTY:
                    continue
                if not self._isValid(data, numForRow[row]) or not self._isValid(data, numForCol[col]):
                    return False
                box = self._boxOf(row, col)
                if not self._isValid(data, numForBox[box]):
                    return False
        return True