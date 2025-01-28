from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        totalOps = 0
        prevOps = 0
        for i in range(len(nums)):
            currentOps = target[i] - nums[i]
            totalOps += max(currentOps - prevOps, 0)
            prevOps = currentOps
        return totalOps + max(-prevOps, 0)
