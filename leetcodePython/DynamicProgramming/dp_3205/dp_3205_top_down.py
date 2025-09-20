from typing import List


class Solution:
    def _maxScoreStartAt(self, startIndex, nums: List[int], maxScoreAt: List[int]) -> int:
        if startIndex == len(nums):
            return 0
        if maxScoreAt[startIndex] != -1:
            return maxScoreAt[startIndex]
        maxScore = 0
        for dstIndex in range(startIndex + 1, len(nums)):
            maxScore = max(maxScore, (dstIndex - startIndex) * nums[dstIndex] + self._maxScoreStartAt(dstIndex, nums, maxScoreAt))

        maxScoreAt[startIndex] = maxScore
        return maxScoreAt[startIndex]

    def maxScore(self, nums: List[int]) -> int:
        maxScoreAt = [-1] * len(nums)
        return self._maxScoreStartAt(0, nums, maxScoreAt)