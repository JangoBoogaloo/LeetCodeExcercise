from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        if len(prices) < 3:
            return max(prices[1]-prices[0], 0)

        maxBalanceSoldAt: List[float] = [float('-inf')] * len(prices)
        maxBalanceHoldAt: List[float] = [float('-inf')] * len(prices)
        maxBalanceRestAt: List[float] = [0] * len(prices)
        maxBalanceHoldAt[0] = -prices[0]

        for day in range(1, len(prices)):
            maxBalanceSoldAt[day] = maxBalanceHoldAt[day-1] + prices[day]
            maxBalanceHoldAt[day] = max(maxBalanceHoldAt[day-1], maxBalanceRestAt[day-1] - prices[day])
            maxBalanceRestAt[day] = max(maxBalanceRestAt[day-1], maxBalanceSoldAt[day-1])
        return int(max(maxBalanceSoldAt[-1], maxBalanceRestAt[-1]))


class SolutionBottomUp:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxBalanceSold = float('-inf')
        maxBalanceHold = -prices[0]
        maxBalanceRest = 0

        for currentPrice in prices[1:]:
            prevSold = maxBalanceSold
            maxBalanceSold = maxBalanceHold + currentPrice
            maxBalanceHold = max(maxBalanceHold, maxBalanceRest - currentPrice)
            maxBalanceRest = max(maxBalanceRest, prevSold)

        return max(maxBalanceSold, maxBalanceRest)