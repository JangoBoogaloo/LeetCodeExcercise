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