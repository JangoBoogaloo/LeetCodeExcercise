from typing import List


class Solution:
    def _maxSumAt(self, startIndex: int, arr:List[int], k: int, maxSumStartAt:List[int]) -> int:
        if startIndex == len(arr):
            return 0
        if maxSumStartAt[startIndex] != -1:
            return maxSumStartAt[startIndex]
        maxNum = 0
        for size in range(min(k, len(arr) - startIndex)):
            maxNum = max(maxNum, arr[startIndex+size])
            subArraySum = maxNum * (size+1)
            concatSum = self._maxSumAt(startIndex+size+1, arr, k, maxSumStartAt)
            maxSumStartAt[startIndex] = max(maxSumStartAt[startIndex], subArraySum + concatSum)
        return maxSumStartAt[startIndex]

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        maxSumStartAt = [-1] * len(arr)
        return self._maxSumAt(0, arr, k, maxSumStartAt)






