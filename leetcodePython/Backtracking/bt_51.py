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

    @staticmethod
    def _get_board(board: List[List[str]]) -> List[str]:
        ans = []
        for row in board:
            ans.append("".join(row))
        return ans

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        solutions = []

        def backtrack(row: int):
            if row == n:
                solutions.append(self._get_board(board))

            for col in range(n):
                if not self._is_valid(row, col, board):
                    continue
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

        backtrack(0)
        return solutions


if __name__ == "__main__":
    sol = Solution()
    ans = sol.solveNQueens(4)
    for a in ans:
        for r in a:
            print(r)
        print()
