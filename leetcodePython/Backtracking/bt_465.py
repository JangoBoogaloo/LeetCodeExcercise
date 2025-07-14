from collections import Counter
from typing import List


class Solution:
    def _transactionAt(self, startIndex: int, balances: List) -> int:
        while startIndex < len(balances) and balances[startIndex] == 0:
            startIndex += 1
        if startIndex == len(balances):
            return 0
        minCost = float("inf")
        for nextIndex in range(startIndex+1, len(balances)):
            if balances[startIndex] * balances[nextIndex] < 0:
                balances[nextIndex] += balances[startIndex]
                cost = 1 + self._transactionAt(startIndex+1, balances)
                minCost = min(minCost, cost)
                balances[nextIndex] -= balances[startIndex]
        return minCost

    def minTransfers(self, transactions: List[List[int]]) -> int:
        balanceMap = Counter()
        for src, dst, amount in transactions:
            balanceMap[src] -= amount
            balanceMap[dst] += amount

        balances = list(balanceMap.values())
        return self._transactionAt(0, balances)






