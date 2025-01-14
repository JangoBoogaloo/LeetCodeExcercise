from typing import List


class SolutionBruteForce:
    def maxScore(self, nums: List[int]) -> int:
        maxStartingAt = [0] * len(nums)
        for j in range(1, len(nums)):
            for i in range(j):
                maxStartingAt[j] = max(maxStartingAt[j], maxStartingAt[i] + (j-i)*nums[j])
        return maxStartingAt[-1]


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        maxScore = 0
        score = 0
        for i in range(len(nums)-1, 0, -1):
            maxScore = max(maxScore, nums[i])
            score += maxScore
        return score
