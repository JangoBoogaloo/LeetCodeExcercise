from typing import List


class SolutionFullDFS:
    def _dfs_check_surround(self, board: List[List[str]], visited: List[List[bool]], region: List[tuple[int, int]],
                            row: int, col: int) -> bool:
        if row < 0 or col < 0:
            return True
        if row >= len(board) or col >= len(board[0]):
            return True
        if visited[row][col] or board[row][col] == "X":
            visited[row][col] = True
            return True

        visited[row][col] = True
        surround = True
        region.append((row, col))
        if row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1:
            surround = False
        surround &= self._dfs_check_surround(board, visited, region, row - 1, col)
        surround &= self._dfs_check_surround(board, visited, region, row + 1, col)
        surround &= self._dfs_check_surround(board, visited, region, row, col - 1)
        surround &= self._dfs_check_surround(board, visited, region, row, col + 1)
        return surround

    def solve(self, board: List[List[str]]) -> None:
        visited = [[False] * len(board[i]) for i in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                region = []
                if self._dfs_check_surround(board, visited, region, row, col):
                    for r, c in region:
                        board[r][c] = "X"
