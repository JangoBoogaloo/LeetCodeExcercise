from typing import List


class Solution:
    def _up_down_flip(self, matrix: List[List[int]], size: int) -> None:
        """
        12  34
        34  12
        """
        up, down = 0, size - 1
        while up < down:
            for col in range(size):
                matrix[up][col], matrix[down][col] = matrix[down][col], matrix[up][col]
            up += 1
            down -= 1

    def _diagonal_flip(self, matrix: List[List[int]], size: int) -> None:
        """
        123     147
        456     258
        789     369
        """
        for row in range(size):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        self._up_down_flip(matrix, size)
        self._diagonal_flip(matrix, size)






import pytest
target = Solution()

@pytest.mark.parametrize("matrix, expect",
[
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
     [[7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]]),
    ([[1]], [[1]]),
    ([], []),
])
def test_rotate(matrix, expect):
    target.rotate(matrix)
    assert matrix == expect