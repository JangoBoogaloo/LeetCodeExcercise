from typing import List
from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sortedUnique = sorted(set(nums))
        minOps = len(nums)
        for left in range(len(sortedUnique)):
            rightVal = sortedUnique[left] + len(nums) - 1
            right = bisect_right(sortedUnique, rightVal)
            continuousCount = right - left
            minOps = min(minOps, len(nums) - continuousCount)
        return minOps