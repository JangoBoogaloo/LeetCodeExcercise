from typing import List


class Solution:
    def _robGainStartAt(self, index, robGainStartAt, nums) -> int:
        if index >= len(nums):
            return 0
        if robGainStartAt[index] != -1:
            return robGainStartAt[index]
        robCurrent = nums[index] + self._robGainStartAt(index+2, robGainStartAt, nums)
        skipCurrent = self._robGainStartAt(index + 1, robGainStartAt, nums)
        robGainStartAt[index] = max(robCurrent, skipCurrent)
        return robGainStartAt[index]

    def rob(self, nums: List[int]) -> int:
        robGainStartAt = [-1] * len(nums)
        return self._robGainStartAt(0, robGainStartAt, nums)





