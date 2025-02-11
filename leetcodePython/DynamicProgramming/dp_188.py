import math
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k == 0:
            return 0

        if k * 2 >= n:
            res = 0
            for day, usedTransaction in zip(prices[1:], prices[:-1]):
                res += max(0, day - usedTransaction)
            return res

        # maxBalance_day_transaction_hold[day][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold

        maxBalanceHoldAt = [[-math.inf] * k for _ in range(n)]
        maxBalanceSoldAt = [[-math.inf] * k for _ in range(n)]

        maxBalanceSoldAt[0][0] = 0
        maxBalanceHoldAt[0][1] = -prices[0]

        # fill the array
        for day in range(1, n):
            for usedTransaction in range(k + 1):
                maxBalanceSoldAt[day][usedTransaction] = self._getCurrentMaxFromSold(day, usedTransaction, prices[day], maxBalanceHoldAt, maxBalanceSoldAt)
                if usedTransaction <= 0:
                    continue
                maxBalanceHoldAt[day][usedTransaction] = self._getCurrentMaxFromHold(day, usedTransaction, prices[day], maxBalanceHoldAt, maxBalanceSoldAt)

        res = max(maxBalanceSoldAt[n - 1][j]for j in range(k + 1))
        return int(res)

    def _getCurrentMaxFromSold(self, day: int, transaction:int, price,  maxBalanceHoldAt: List[List[float]], maxBalanceSoldAt: List[List[float]]) -> float:
        return max(maxBalanceSoldAt[day - 1][transaction], maxBalanceHoldAt[day - 1][transaction] + price)

    def _getCurrentMaxFromHold(self, day: int, transaction:int, price,  maxBalanceHoldAt: List[List[float]], maxBalanceSoldAt: List[List[float]]) -> float:
        return max(maxBalanceSoldAt[day - 1][transaction-1] - price, maxBalanceHoldAt[day - 1][transaction])
