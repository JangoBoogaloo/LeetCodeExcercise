from typing import List
from collections import Counter


class Solution:
    def maxChunksToSorted(self, arr: List[int]):
        actual_vs_expect = Counter()
        balancedCount = balance = 0

        for x, y in zip(arr, sorted(arr)):
            actual_vs_expect[x] += 1
            if actual_vs_expect[x] == 0:
                balance -= 1
            if actual_vs_expect[x] == 1:
                balance += 1
            actual_vs_expect[y] -= 1
            if actual_vs_expect[y] == -1:
                balance += 1
            if actual_vs_expect[y] == 0:
                balance -= 1
            if balance == 0:
                balancedCount +=1
        return balancedCount








