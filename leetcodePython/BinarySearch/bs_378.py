from typing import List


class Solution:
    @staticmethod
    def _countLessEqual(x:int, matrix: List[List[int]]) -> int:
        count = 0
        colRight = len(matrix[0])-1
        for i in range(len(matrix)):
            while colRight >= 0 and matrix[i][colRight] > x:
                colRight -= 1
            count += colRight + 1
        return count

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]
        while left < right:
            mid = (left + right) // 2
            if self._countLessEqual(mid, matrix) < k:
                left = mid + 1
            else:
                right = mid
        return left
