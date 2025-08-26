from typing import List


class Solution:
    def _waysStartAtStairs(self, stair: int, waysStartAt: List[int], endStairs: int):
        if stair > endStairs:
            return 0
        if stair == endStairs:
            return 1
        if waysStartAt[stair]:
            return waysStartAt[stair]
        waysStartAt[stair] = self._waysStartAtStairs(stair+1, waysStartAt, endStairs) + self._waysStartAtStairs(stair+2, waysStartAt, endStairs)
        return waysStartAt[stair]

    def climbStairs(self, n: int) -> int:
        waysStartAt = [0] * (n + 1)
        return self._waysStartAtStairs(0, waysStartAt, n)





