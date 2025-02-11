from typing import List


class Solution:
    def maxProfit(self, transaction: int, prices: List[int]) -> int:
        if transaction == 0:
            return 0
        minCostAtTransaction: List[float]
        minCostAtTransaction = [float("inf")] * (transaction+1)
        maxProfitAtTransaction: List[float]
        maxProfitAtTransaction = [0] * (transaction + 1)

        for price in prices:
            for t in range(1, transaction + 1):
                minCostAtTransaction[t] = min(minCostAtTransaction[t], price - maxProfitAtTransaction[t-1])
                maxProfitAtTransaction[t] = max(maxProfitAtTransaction[t], price - minCostAtTransaction[t])

        return int(maxProfitAtTransaction[transaction])
