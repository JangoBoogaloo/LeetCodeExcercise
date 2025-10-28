from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        maxSumEndAt = [0] * (len(arr) + 1)
        for end in range(1, len(maxSumEndAt)):
            currMax = 0
            for size in range(1, min(k, end)+1):
                currMax = max(currMax, arr[end-size])
                maxSumEndAt[end] = max(maxSumEndAt[end], maxSumEndAt[end-size] + currMax * size)
        return maxSumEndAt[-1]








