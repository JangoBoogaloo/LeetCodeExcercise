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









