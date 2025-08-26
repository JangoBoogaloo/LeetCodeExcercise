class Solution:
    def climbStairs(self, n: int) -> int:
        ways1StepBefore, ways2StepsBefore = 1, 1
        currentWays = 1
        for i in range(2, n + 1):
            currentWays = ways1StepBefore + ways2StepsBefore
            ways1StepBefore, ways2StepsBefore = currentWays, ways1StepBefore
        return currentWays