from typing import List


class Solution:

    @staticmethod
    def _minSum(nums: List[int]) -> int:
        increaseIndexStack = []
        length = len(nums)
        minSum = 0
        for right in range(length + 1):
            while increaseIndexStack and (right == length or nums[right] <= nums[increaseIndexStack[-1]]):
                minMidIndex = increaseIndexStack.pop()
                left = -1 if not increaseIndexStack else increaseIndexStack[-1]
                minUsageCount = (right - minMidIndex) * (minMidIndex - left)
                minSum += nums[minMidIndex] * minUsageCount
            increaseIndexStack.append(right)
        return minSum

    @staticmethod
    def _maxSum(nums: List[int]) -> int:
        decreaseIndexStack = []
        length = len(nums)
        maxSum = 0
        for right in range(length + 1):
            while decreaseIndexStack and (right == length or nums[right] >= nums[decreaseIndexStack[-1]]):
                maxMidIndex = decreaseIndexStack.pop()
                left = -1 if not decreaseIndexStack else decreaseIndexStack[-1]
                maxUsageCount = (right - maxMidIndex) * (maxMidIndex - left)
                maxSum += nums[maxMidIndex] * maxUsageCount
            decreaseIndexStack.append(right)
        return maxSum

    def subArrayRanges(self, nums: List[int]) -> int:
        return self._maxSum(nums) - self._minSum(nums)


class SolutionBruteForce:
    def _getRange(self, nums: List[int]) -> int:
        return max(nums) - min(nums)

    def subArrayRanges(self, nums: List[int]) -> int:
        sumRange = 0
        for end in range(len(nums)):
            for start in range(end+1):
                sumRange += self._getRange(nums[start:end+1])
        return sumRange
