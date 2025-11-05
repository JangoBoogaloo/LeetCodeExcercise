from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCountToGet = [float("inf")] * (amount + 1)
        minCountToGet[0] = 0
        for coin in coins:
            for target in range(coin, amount + 1):
                minCountToGet[target] = min(minCountToGet[target], minCountToGet[target-coin] + 1)
        if minCountToGet[amount] == float("inf"):
            return -1
        return minCountToGet[amount]


class SolutionTopDown:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        minCountToGet = [float("inf")] * (amount + 1)
        minCountToGet[0] = 0
        return self._coinChange(coins, amount, minCountToGet)

    def _coinChange(self, coins: List[int], amount: int, minCountToGet: List[int]):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if minCountToGet[amount] != float("inf"):
            return minCountToGet[amount]
        minCount = float("inf")
        for coin in coins:
            count = self._coinChange(coins, amount-coin, minCountToGet)
            if 0 <= count < minCount:
                minCount = count + 1
        if minCount == float("inf"):
            minCountToGet[amount] = -1
        else:
            minCountToGet[amount] = minCount
        return minCountToGet[amount]


class SolutionBruteForce:
    @staticmethod
    def coinChange(coins: List[int], amount: int) -> int:
        coins.sort()
        minCount = float("inf")

        def backtrack(target: int, count: int) -> int:
            if target < 0:
                return float("inf")
            if target == 0:
                return count
            nonlocal minCount
            for coin in coins:
                minCount = min(minCount, backtrack(target - coin, count + 1))
            return minCount

        ans = backtrack(amount, 0)
        if ans == float("inf"):
            return -1
        return ans
