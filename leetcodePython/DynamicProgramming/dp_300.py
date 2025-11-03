from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLengthEndAt = [1] * len(nums)
        for right in range(1, len(nums)):
            for left in range(right):
                if nums[left] < nums[right]:
                    newLength = maxLengthEndAt[left] + 1
                    maxLengthEndAt[right] = max(maxLengthEndAt[right], newLength)
        return max(maxLengthEndAt)
