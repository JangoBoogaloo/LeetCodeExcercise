from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        size = len(nums)
        result = 0
        for i in range(size):
            j = self.binarySearchIndexWithTargetDiff(nums, i+1, size-1, nums[i]+diff)
            if j < 0:
                continue
            k = self.binarySearchIndexWithTargetDiff(nums, j+1, size-1, nums[j]+diff)
            if k < 0:
                continue
            result += 1
        return result

    def binarySearchIndexWithTargetDiff(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = left + int((right - left) / 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
