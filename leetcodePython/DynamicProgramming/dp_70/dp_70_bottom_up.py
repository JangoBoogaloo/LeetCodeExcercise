class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        waysToStairs = [1] * (n + 1)
        for i in range(2, n + 1):
            waysToStairs[i] = waysToStairs[i-1] + waysToStairs[i-2]
        return waysToStairs[n]





