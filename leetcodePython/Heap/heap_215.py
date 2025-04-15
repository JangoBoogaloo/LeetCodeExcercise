from heapq import nlargest, heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]


class SolutionDetailed:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kLargest = []
        for num in nums:
            heappush(kLargest, num)
            if len(kLargest) > k:
                heappop(kLargest)
        return kLargest[0]
