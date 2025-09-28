from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxDst = 0
        for pos in range(len(nums)):
            if pos > maxDst:
                return False
            maxDst = max(maxDst, pos + nums[pos])
            if maxDst >= len(nums) -1:
                return True
        return maxDst >= len(nums) -1






