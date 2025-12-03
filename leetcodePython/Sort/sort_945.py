from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        totalMoves = 0
        for i in range(1, len(nums)):
            moves = max(0, nums[i-1] + 1 - nums[i])
            nums[i] += moves
            totalMoves += moves
        return totalMoves
