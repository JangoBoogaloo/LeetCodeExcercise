from collections import Counter
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balanceMap = Counter()
        for src, dst, amount in transactions:
            balanceMap[src] -= amount
            balanceMap[dst] += amount
        balances = [amount for amount in balanceMap.values() if amount != 0]

        zeroSumSetCount = [0] * (2**len(balances))
        sumAtMask = [0] * (2**len(balances))

        for mask in range(2**len(balances)):
            setBit = 1
            for amount in balances:
                if mask & setBit == 0:
                    nextMask = mask | setBit
                    sumAtMask[nextMask] = sumAtMask[mask] + amount
                    if sumAtMask[nextMask] == 0:
                        zeroSumSetCount[nextMask] = max(zeroSumSetCount[nextMask], zeroSumSetCount[mask] + 1)
                    else:
                        zeroSumSetCount[nextMask] = max(zeroSumSetCount[nextMask], zeroSumSetCount[mask])
                setBit <<= 1
        return len(balances) - zeroSumSetCount[-1]










