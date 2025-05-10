from typing import List
from sortedcontainers import SortedSet

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = k * (k + 1) // 2
        for num in SortedSet(nums):
            if k >= num:
                k += 1
                ans += k - num
        return ans