from typing import List


class SolutionBruteForce:
    def maxScore(self, nums: List[int]) -> int:
        maxStartingAt = [0] * len(nums)
        for j in range(1, len(nums)):
            for i in range(j):
                maxStartingAt[j] = max(maxStartingAt[j], maxStartingAt[i] + (j-i)*nums[j])
        return maxStartingAt[-1]