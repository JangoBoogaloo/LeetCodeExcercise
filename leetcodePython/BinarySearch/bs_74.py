from bisect import bisect_left
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_min = matrix[0][0]
        matrix_max = matrix[-1][-1]
        if target < matrix_min or target > matrix_max:
            return False

        row_idx = bisect_left(matrix, target, key=lambda x: x[-1])
        target_row = matrix[row_idx]
        target_index = bisect_left(target_row, target)
        if target_index == len(target_row):
            return False
        return target_row[target_index] == target