from typing import List
from heapq import heappop,  heappush

class Solution:
    _MOD = 10 ** 9 + 7
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sortedSum = []
        for i in range(n):
            heappush(sortedSum, (nums[i], i))
        total = 0
        for i in range(1, right + 1):
            currSum, currSumIndex = heappop(sortedSum)
            if i >= left:
                total += currSum
            if currSumIndex < n - 1:
                heappush(sortedSum, (currSum + nums[currSumIndex + 1], currSumIndex + 1))
        return total % self._MOD






