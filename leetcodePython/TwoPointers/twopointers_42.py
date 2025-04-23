from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftWall, rightWall = 0, 0
        left, right = 0, len(height) - 1
        rain = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < leftWall:
                    rain += leftWall - height[left]
                else:
                    leftWall = height[left]
                left += 1
            else:
                if height[right] < rightWall:
                    rain += rightWall - height[right]
                else:
                    rightWall = height[right]
                right -= 1
        return rain
