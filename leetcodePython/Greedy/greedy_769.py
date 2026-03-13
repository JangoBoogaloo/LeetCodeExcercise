from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        currMax = 0
        matchMaxCount = 0
        for i, num in enumerate(arr):
            currMax = max(currMax, num)
            expectedMax = i
            if currMax == expectedMax:
                matchMaxCount += 1
        return matchMaxCount






