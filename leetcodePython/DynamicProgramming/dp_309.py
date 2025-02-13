from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        if len(prices) < 3:
            return max(prices[1]-prices[0], 0)

        maxBalanceSoldAt: List[float] = [float('-inf')] * len(prices)
        maxBalanceHoldAt: List[float] = [float('-inf')] * len(prices)
        maxBalanceResetAt: List[float] = [0] * len(prices)
        maxBalanceHoldAt[0] = -prices[0]

        for day in range(1, len(prices)):
            maxBalanceSoldAt[day] = maxBalanceHoldAt[day-1] + prices[day]
            maxBalanceHoldAt[day] = max(maxBalanceHoldAt[day-1], maxBalanceResetAt[day-1] - prices[day])
            maxBalanceResetAt[day] = max(maxBalanceResetAt[day-1], maxBalanceSoldAt[day-1])
        return int(max(maxBalanceSoldAt[-1], maxBalanceResetAt[-1]))
