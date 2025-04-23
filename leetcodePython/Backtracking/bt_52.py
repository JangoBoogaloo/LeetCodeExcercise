from typing import List


class Solution:
    @staticmethod
    def _is_valid(row: int, col: int, board: List[List[str]]) -> bool:
        """
           *
           *
        ...X...
        """
        for r in range(row - 1, -1, -1):
            if board[r][col] == "Q":
                return False

        """
         *
          *
        ...X...
        """
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        """
             *
            *
        ...X...
        """
        r, c = row - 1, col + 1
        while r >= 0 and c < len(board[0]):
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        return True

    _answers = 0

    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for _ in range(n)]
        _answers = 0

        def backtrack(row: int):
            if row == n:
                self._answers += 1

            for col in range(n):
                if not self._is_valid(row, col, board):
                    continue
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

        backtrack(0)

        return self._answers
