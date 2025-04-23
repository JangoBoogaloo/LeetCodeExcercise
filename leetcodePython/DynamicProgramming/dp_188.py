from typing import List


class SolutionMaxBalance:
    def _maxProfitUnlimitedTransaction(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit

    def maxProfit(self, transaction: int, prices: List[int]) -> int:
        if not prices or transaction == 0:
            return 0

        if transaction * 2 >= len(prices):
            return self._maxProfitUnlimitedTransaction(prices)

        maxBalanceHoldAt = [[-float("inf")] * (transaction+1) for _ in range(len(prices))]
        maxBalanceSoldAt = [[-float("inf")] * (transaction+1) for _ in range(len(prices))]

        maxBalanceHoldAt[0][1] = -prices[0]
        maxBalanceSoldAt[0][0] = 0

        for day in range(1, len(prices)):
            for trans in range(transaction + 1):
                maxBalanceSoldAt[day][trans] = max(maxBalanceHoldAt[day-1][trans]+prices[day], maxBalanceSoldAt[day-1][trans])
                if not trans:
                    continue
                maxBalanceHoldAt[day][trans] = max(maxBalanceHoldAt[day-1][trans], maxBalanceSoldAt[day-1][trans-1] - prices[day])
        return int(max(maxBalanceSoldAt[-1][t] for t in range(transaction + 1)))


class SolutionMinCostMaxGain:
    def maxProfit(self, transaction: int, prices: List[int]) -> int:
        if transaction == 0:
            return 0
        minCostAtTransaction: List[float]
        minCostAtTransaction = [float("inf")] * (transaction+1)
        maxGainAtTransaction: List[float]
        maxGainAtTransaction = [0] * (transaction + 1)

        for price in prices:
            for t in range(1, transaction + 1):
                minCostAtTransaction[t] = min(minCostAtTransaction[t], price - maxGainAtTransaction[t-1])
                maxGainAtTransaction[t] = max(maxGainAtTransaction[t], price - minCostAtTransaction[t])

        return int(maxGainAtTransaction[transaction])
