from typing import List


class Solution:
    @staticmethod
    def _getMinimumUnsortedLeftIndex(nums: List[int]) -> int:
        breakMonotonicIndex = len(nums)
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                breakMonotonicIndex = i
                break

        if breakMonotonicIndex == len(nums):
            return len(nums)

        unsortedMin = min(nums[breakMonotonicIndex:])

        for left in range(len(nums)):
            if nums[left] > unsortedMin:
                return left
        return len(nums)

    @staticmethod
    def _getMaximumUnsortedRightIndex(nums: List[int]) -> int:
        breakMonotonicIndex = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                breakMonotonicIndex = i
                break
        if breakMonotonicIndex == -1:
            return -1
        unsortedMax = max(nums[:breakMonotonicIndex+1])
        for right in range(len(nums) - 1, -1, -1):
            if unsortedMax > nums[right]:
                return right
        return -1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = self._getMinimumUnsortedLeftIndex(nums)
        right = self._getMaximumUnsortedRightIndex(nums)
        return right - left + 1 if right > left else 0
