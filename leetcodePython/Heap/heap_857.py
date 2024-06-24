from typing import List
from heapq import heappush, heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        sorted_wq_ratios = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        min_pay = float("inf")
        quality_sum = 0
        hired_quality_max_heap = []
        for r, q in sorted_wq_ratios:
            heappush(hired_quality_max_heap, -q)
            quality_sum += q
            if len(hired_quality_max_heap) > k:
                max_quality = -heappop(hired_quality_max_heap)
                quality_sum -= max_quality
            if len(hired_quality_max_heap) == k:
                min_pay = min(min_pay, quality_sum * r)
        return min_pay