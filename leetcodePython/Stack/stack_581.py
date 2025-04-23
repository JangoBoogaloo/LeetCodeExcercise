from typing import List


class Solution:
    @staticmethod
    def _getMinimumUnsortedLeftIndex(nums: List[int]) -> int:
        left = len(nums)
        increaseNumIndexStack = []
        for i in range(len(nums)):
            while increaseNumIndexStack and nums[i] < nums[increaseNumIndexStack[-1]]:
                left = min(left, increaseNumIndexStack.pop())
            increaseNumIndexStack.append(i)
        return left

    @staticmethod
    def _getMaximumUnsortedRightIndex(nums: List[int]) -> int:
        decreaseNumIndexStack = []
        right = 0
        for i in range(len(nums)-1, -1, -1):
            while decreaseNumIndexStack and nums[i] > nums[decreaseNumIndexStack[-1]]:
                right = max(right, decreaseNumIndexStack.pop())
            decreaseNumIndexStack.append(i)
        return right

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = self._getMinimumUnsortedLeftIndex(nums)
        right = self._getMaximumUnsortedRightIndex(nums)
        return right - left + 1 if right > left else 0
