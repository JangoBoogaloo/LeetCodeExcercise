from typing import List


class SolutionSort:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums[:])
        right = -1
        left = 0
        for i in range(len(nums)):
            if nums[i] != sortedNums[i]:
                left = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != sortedNums[i]:
                right = i
                break

        return right - left + 1


class SolutionStack:
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


class Solution:
    @staticmethod
    def _getMinimumUnsortedLeftIndex(nums: List[int]) -> int:
        breakMonotonicIndex = len(nums)
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                breakMonotonicIndex = i
                break

        unsortedMin = float("inf")
        for i in range(breakMonotonicIndex, len(nums)):
            unsortedMin = min(unsortedMin, nums[i])

        for left in range(len(nums)):
            if unsortedMin < nums[left]:
                return left
        return len(nums)

    @staticmethod
    def _getMaximumUnsortedRightIndex(nums: List[int]) -> int:
        breakMonotonicIndex = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                breakMonotonicIndex = i
                break

        unsortedMax = float("-inf")
        for i in range(breakMonotonicIndex, -1, -1):
            unsortedMax = max(unsortedMax, nums[i])

        for right in range(len(nums)-1, -1, -1):
            if unsortedMax > nums[right]:
                return right
        return -1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = self._getMinimumUnsortedLeftIndex(nums)
        right = self._getMaximumUnsortedRightIndex(nums)
        return right - left + 1 if right > left else 0
