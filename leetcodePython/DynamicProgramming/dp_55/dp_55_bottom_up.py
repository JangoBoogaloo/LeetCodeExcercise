from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachEndFrom = [False] * len(nums)
        reachEndFrom[-1] = True
        for src in range(len(nums) - 2, -1, -1):
            dstRange = min(len(nums)-1, src + nums[src])
            for dst in range(src+1, dstRange+1):
                if reachEndFrom[dst]:
                    reachEndFrom[src] = True
                    break
        return reachEndFrom[0]





