from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        histogram = [0]*len(matrix[0])
        for row in range(len(matrix)):
            self._updateHistogramForRow(row, matrix, histogram)
            currMaxArea = self._largestHistogramRectangle(histogram)
            maxArea = max(maxArea, currMaxArea)
        return maxArea

    @staticmethod
    def _updateHistogramForRow(row: int, matrix: List[List[str]], histogram: List[int]) -> None:
        for col in range(len(matrix[0])):
            if matrix[row][col] == '1':
                histogram[col] = histogram[col] + 1
            else:
                histogram[col] = 0

    @staticmethod
    def _largestHistogramRectangle(heights: List[int]) -> int:
        increaseHeightIndex = [-1]
        maxArea = 0
        heights.append(0)
        for i in range(len(heights)):
            newHeight = heights[i]
            while increaseHeightIndex[-1] != -1:
                maxHeight = heights[increaseHeightIndex[-1]]
                if newHeight > maxHeight:
                    break
                increaseHeightIndex.pop()
                smallerHeightIndex = increaseHeightIndex[-1]
                width = i - smallerHeightIndex - 1
                maxArea = max(maxArea, maxHeight*width)
            increaseHeightIndex.append(i)
        heights.pop()
        return maxArea
