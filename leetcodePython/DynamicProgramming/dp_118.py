from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        triangle.append([1])
        if numRows == 1:
            return triangle
        triangle.append([1,1])
        if numRows == 2:
            return triangle

        for r in range(2, numRows):
            row = [1]
            prev_row = triangle[r-1]
            for c in range(1, r):
                row.append(prev_row[c-1] + prev_row[c])
            row.append(1)
            triangle.append(row)
        return triangle