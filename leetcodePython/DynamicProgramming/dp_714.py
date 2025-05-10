from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) < 2:
            return 0
        maxBalanceHold, maxBalanceSold = -prices[0], 0
        for price in prices[1:]:
            maxBalanceSold = max(maxBalanceHold+price-fee, maxBalanceSold)
            maxBalanceHold = max(maxBalanceSold-price, maxBalanceHold)
        return maxBalanceSold
