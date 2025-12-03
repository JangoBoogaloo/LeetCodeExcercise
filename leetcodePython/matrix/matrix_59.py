from typing import List


class Solution:
    @staticmethod
    def _valid(newR, newC, matrix) -> bool:
        if newR < 0 or newR >= len(matrix):
            return False
        if newC < 0 or newC >= len(matrix[0]):
            return False
        return matrix[newR][newC] == 0

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pos = (0, 0)
        directionIndex = 0
        matrix[0][0] = 1
        currNum = 2

        direction = directions[directionIndex]

        while True:
            newR, newC = pos[0] + direction[0], pos[1] + direction[1]
            if self._valid(newR, newC, matrix):
                matrix[newR][newC] = currNum
                currNum += 1
                pos = (newR, newC)
            else:
                directionIndex = (directionIndex+1) % len(directions)
                direction = directions[directionIndex]
                newR, newC = pos[0] + direction[0], pos[1] + direction[1]
                if not self._valid(newR, newC, matrix):
                    break
        return matrix







