from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0] * 3
        for num in nums:
            colors[num] += 1
        colorIndex = 0
        for i in range(len(nums)):
            while colors[colorIndex] < 1:
                colorIndex += 1
            nums[i] = colorIndex
            colors[colorIndex] -= 1





