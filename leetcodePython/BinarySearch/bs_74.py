from typing import List
from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        minimum, maximum = matrix[0][0], matrix[-1][-1]
        if target < minimum or target > maximum:
            return False
        rowIndex = bisect_left(matrix, target, key=lambda x: x[-1])
        colIndex = bisect_left(matrix[rowIndex], target)
        if colIndex == len(matrix[rowIndex]):
            return False
        return matrix[rowIndex][colIndex] == target










import pytest
sol = Solution()

@pytest.mark.parametrize("matrix, target, expect",
[
    ([
        [1,2,3],
        [4],
        [5,6],
        [7,8,9,10]
     ], 6, True),
    ([
         [1, 2, 3],
         [4],
         [5, 7],
         [7, 8, 9, 10]
     ], 6, False),
])
def test_searchMatrix(matrix, target, expect):
    assert sol.searchMatrix(matrix, target) == expect