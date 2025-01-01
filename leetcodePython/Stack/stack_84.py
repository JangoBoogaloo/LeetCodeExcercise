from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
                maxArea = max(maxArea, maxHeight * width)
            increaseHeightIndex.append(i)
        heights.pop()
        return maxArea


if __name__ == '__main__':
    solution = Solution()
    solution.largestRectangleArea([1])