from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        bigger = 0
        result = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                bigger = nums[right]
                right -= 1
            else:
                bigger = nums[left]
                left += 1
            result[i] = bigger*bigger
        return result