from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        maxBalanceHold, maxBalanceSold = -prices[0], 0
        for price in prices[1:]:
            maxBalanceHold = max(maxBalanceHold, maxBalanceSold - price)
            maxBalanceSold = max(maxBalanceHold + price, maxBalanceSold)
        return maxBalanceSold
