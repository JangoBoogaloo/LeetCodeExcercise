from typing import List


class Solution:
    def _isBorder(self, row, col, sidePoints) -> bool:
        if row == 0 or row == sidePoints-1 or col == 0 or col == sidePoints - 1:
            return True
        return False

    def _registerBorderPoints(self, sidePoints: int, uf):
        for row in range(sidePoints):
            for col in range(sidePoints):
                if self._isBorder(row, col, sidePoints):
                    id = row * sidePoints + col
                    uf.registerParent(id, 0)

    def regionsBySlashes(self, grid: List[str]) -> int:
        sidePoints = len(grid) + 1
        uf = UF(sidePoints * sidePoints)
        self._registerBorderPoints(sidePoints, uf)
        uf.registerParent(0, -1)
        components = 1
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == '/':
                    firstPoint = topRight = row * sidePoints + col + 1
                    secondPoint = bottomLeft = (row + 1) * sidePoints + col
                elif grid[row][col] == '\\':
                    firstPoint = topLeft = row * sidePoints + col
                    secondPoint = bottomRight = (row + 1) * sidePoints + col + 1
                else:
                    continue
                if not uf.union(firstPoint, secondPoint):
                    components += 1
        return components

class UF:
    def __init__(self, size: int):
        self.parents = [-1] * size

    def registerParent(self, a: int, parent: int) -> None:
        self.parents[a] = parent

    def find(self, a: int) -> int:
        if self.parents[a] == -1:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        self.parents[root_b] = root_a
        return True