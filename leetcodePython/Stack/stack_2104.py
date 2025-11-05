from typing import List


class Solution:
    @staticmethod
    def _minSum(nums: List[int]) -> int:
        increaseIndexStack = []
        minSum = 0
        nums.append(float('-inf'))
        for right in range(len(nums)):
            currNum = nums[right]
            while increaseIndexStack and currNum <= nums[increaseIndexStack[-1]]:
                minIndex = increaseIndexStack.pop()
                lessThanMinIndex = -1 if not increaseIndexStack else increaseIndexStack[-1]
                minUsageCount = (right - minIndex) * (minIndex - lessThanMinIndex)
                minSum += nums[minIndex] * minUsageCount
            increaseIndexStack.append(right)
        nums.pop()
        return minSum

    @staticmethod
    def _maxSum(nums: List[int]) -> int:
        decreaseIndexStack = []
        maxSum = 0
        nums.append(float('inf'))
        for right in range(len(nums)):
            currNum = nums[right]
            while decreaseIndexStack and currNum >= nums[decreaseIndexStack[-1]]:
                maxIndex = decreaseIndexStack.pop()
                moreThanMaxIndex = -1 if not decreaseIndexStack else decreaseIndexStack[-1]
                maxUsageCount = (right - maxIndex) * (maxIndex - moreThanMaxIndex)
                maxSum += nums[maxIndex] * maxUsageCount
            decreaseIndexStack.append(right)
        nums.pop()
        return maxSum

    def subArrayRanges(self, nums: List[int]) -> int:
        return self._maxSum(nums) - self._minSum(nums)