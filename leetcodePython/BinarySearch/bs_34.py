from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startIndex = bisect_left(nums, target)
        if startIndex == len(nums):
            return [-1, -1]
        endIndex = bisect_right(nums, target) - 1
        if endIndex == -1:
            return [-1, -1]
        if nums[startIndex] != target:
            return [-1, -1]
        return [startIndex, endIndex]








