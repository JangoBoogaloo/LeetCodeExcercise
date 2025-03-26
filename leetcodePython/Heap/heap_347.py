import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums
        numFreq = Counter(nums)
        return heapq.nlargest(k, numFreq.keys(), key=numFreq.get)


class SolutionDetailed:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums
        numFreq = Counter(nums)
        minFreqQueue = []

        for num in numFreq:
            heapq.heappush(minFreqQueue, (numFreq[num], num))
            while len(minFreqQueue) > k:
                heapq.heappop(minFreqQueue)
        answer = [num for _, num in minFreqQueue]
        return answer