from typing import List


class Solution:
    @staticmethod
    def _rob(nums: List[int]) -> int:
        prevPrevMax = 0
        prevMax = nums[0]
        currentMax = 0
        for num in nums[1:]:
            currentMax = max(num+prevPrevMax, prevMax)
            prevPrevMax = prevMax
            prevMax = currentMax
        return currentMax

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))
