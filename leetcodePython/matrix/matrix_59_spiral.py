from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        row, col = 0, 0
        dr, dc = 0, 1
        for num in range(n*n):
            matrix[row][col] = num + 1
            nr = (row + dr) % n
            nc = (col + dc) % n
            if matrix[nr][nc] != 0:
                # [(0, 1), (1, 0), (0, -1), (-1, 0)]
                dr, dc = dc, -dr
            row += dr
            col += dc
        return matrix







