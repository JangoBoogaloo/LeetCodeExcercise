from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        maxScoreEndAt = [0] * len(nums)
        for endIndex in range(1, len(nums)):
            for startIndex in range(endIndex):
                maxScoreEndAt[endIndex] = max(maxScoreEndAt[endIndex], maxScoreEndAt[startIndex] + (endIndex - startIndex) * nums[endIndex])
        return maxScoreEndAt[-1]