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
        maxBalance_day_transaction_hold = [[[-math.inf] * 2 for _ in range(k + 1)] for _ in range(n)]

        # set starting value
        maxBalance_day_transaction_hold[0][0][0] = 0
        maxBalance_day_transaction_hold[0][1][1] = -prices[0]

        # fill the array
        for day in range(1, n):
            for usedTransaction in range(k + 1):
                # transition equation
                maxBalance_day_transaction_hold[day][usedTransaction][0] = (
                    max(maxBalance_day_transaction_hold[day - 1][usedTransaction][0],
                        maxBalance_day_transaction_hold[day - 1][usedTransaction][1] + prices[day]))
                # you can't hold stock without any transaction
                if usedTransaction > 0:
                    maxBalance_day_transaction_hold[day][usedTransaction][1] = max(
                        maxBalance_day_transaction_hold[day - 1][usedTransaction][1],
                        maxBalance_day_transaction_hold[day - 1][usedTransaction - 1][0] - prices[day]
                    )

        res = max(maxBalance_day_transaction_hold[n - 1][j][0] for j in range(k + 1))
        return res
