from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        maxScoreFromEnd = 0
        totalScore = 0
        for index in range(len(nums) - 1, 0, -1):
            maxScoreFromEnd = max(maxScoreFromEnd, nums[index])
            totalScore += maxScoreFromEnd
        return totalScore







