from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cityUsedCounts = [0]*n
        for c1, c2 in roads:
            cityUsedCounts[c1] += 1
            cityUsedCounts[c2] += 1
        cityUsedCounts.sort()

        importanceRank = 1
        total = 0
        for usedCount in cityUsedCounts:
            total += usedCount*importanceRank
            importanceRank += 1
        return total






