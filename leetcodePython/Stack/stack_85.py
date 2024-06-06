from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        increase_stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            new_height = heights[i]
            while increase_stack[-1] != -1 and heights[increase_stack[-1]] >= new_height:
                current_height = heights[increase_stack.pop()]
                prev_height_index = increase_stack[-1]
                current_width = i - prev_height_index - 1
                max_area = max(max_area, current_height * current_width)
            increase_stack.append(i)

        while increase_stack[-1] != -1:
            current_height = heights[increase_stack.pop()]
            prev_height_index = increase_stack[-1]
            current_width = len(heights) - prev_height_index - 1
            max_area = max(max_area, current_height * current_width)
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        row_histogram = [0]*len(matrix[0])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    row_histogram[col] = row_histogram[col] + 1
                else:
                    row_histogram[col] = 0
            max_area = max(max_area, self.largestRectangleArea(row_histogram))
        return max_area