from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = 0, 0
        left, right = 0, len(height) - 1
        rain = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < leftMax:
                    rain += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    rain += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return rain
