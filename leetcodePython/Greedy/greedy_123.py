from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost1 = minCost2 = float("inf")
        maxProfit1 = maxProfit = 0
        for price in prices:
            minCost1 = min(minCost1, price)
            maxProfit1 = max(maxProfit1, price - minCost1)
            minCost2 = min(minCost2, price - maxProfit1)
            maxProfit = max(maxProfit, price - minCost2)
        return maxProfit






