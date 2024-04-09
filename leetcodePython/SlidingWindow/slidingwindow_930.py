from typing import List


class Solution:
    def _numSubarrayWithAtMostSum(self, nums: List[int], goal: int) -> int:
        ans = left = sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            while left <= right and sum > goal:
                sum -= nums[left]
                left += 1
            ans += right - left + 1
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self._numSubarrayWithAtMostSum(nums, goal) - self._numSubarrayWithAtMostSum(nums, goal - 1)
