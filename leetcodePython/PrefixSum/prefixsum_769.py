from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedSum = currSum = 0
        matchedSumCount = 0
        for i, num in enumerate(arr):
            sortedSum += i
            currSum += num
            if currSum == sortedSum:
                matchedSumCount += 1
        return matchedSumCount






