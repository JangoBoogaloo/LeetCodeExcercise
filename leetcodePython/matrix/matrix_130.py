from typing import List


class Solution:
    _NOT_SURROUND_MASK = "@"
    _DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    @staticmethod
    def _isValid(row, col, board: List[List[str]]) -> bool:
        if row < 0 or row > len(board) -1:
            return False
        if col < 0 or col > len(board[0]) -1:
            return False
        return board[row][col] == "O"

    def _dfsGetEdgeComponent(self, row, col, board: List[List[str]]):
        if not self._isValid(row, col, board):
            return
        board[row][col] = self._NOT_SURROUND_MASK
        for dirR, dirC in self._DIRECTIONS:
            newRow, newCol = row+dirR, col+dirC
            self._dfsGetEdgeComponent(newRow, newCol, board)

    def solve(self, board: List[List[str]]) -> None:
        for row in range(len(board)):
            self._dfsGetEdgeComponent(row, 0, board)
            self._dfsGetEdgeComponent(row, len(board[0])-1, board)
        for col in range(len(board[0])):
            self._dfsGetEdgeComponent(0, col, board)
            self._dfsGetEdgeComponent(len(board)-1, col, board)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == self._NOT_SURROUND_MASK:
                    board[row][col] = "O"