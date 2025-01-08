from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        rightMax = [0] * len(nums)
        rightMax[len(nums) - 1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i])

        left = 0
        maxWidth = 0
        for right in range(len(nums)):
            while left < right and nums[left] > rightMax[right]:
                left += 1
            maxWidth = max(maxWidth, right - left)

        return maxWidth
