from typing import List
from heapq import heappush, heappop

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap, maxHeap = [], []
        maxLength = 0
        left = 0
        for right in range(len(nums)):
            heappush(minHeap, (nums[right], right))
            heappush(maxHeap, (-nums[right], right))
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                left = min(maxHeap[0][1], minHeap[0][1]) + 1
                while maxHeap[0][1] < left:
                    heappop(maxHeap)
                while minHeap[0][1] < left:
                    heappop(minHeap)
            maxLength = max(maxLength, right - left + 1)
        return maxLength