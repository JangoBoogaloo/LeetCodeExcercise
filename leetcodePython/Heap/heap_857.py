from typing import List
from heapq import heappush, heappop


class Solution:
    def mincostToHireWorkers(self, qualities: List[int], wages: List[int], k: int) -> float:
        ratio_quality = sorted((float(pay)/quality, quality) for pay, quality in zip(wages, qualities))
        minPay = float("inf")
        maxQualityHeap = []
        qualitySum = 0

        for currentMaxRatio, quality in ratio_quality:
            heappush(maxQualityHeap, -quality)
            qualitySum += quality
            if len(maxQualityHeap) > k:
                maxQuality = -heappop(maxQualityHeap)
                qualitySum -= maxQuality
            if len(maxQualityHeap) == k:
                minPay = min(minPay, qualitySum * currentMaxRatio)
        return minPay
