from typing import List
from heapq import *


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []
        for i in range(len(arr) - 1):
            heappush(min_heap, (arr[i] / arr[-1], i, len(arr) - 1))
        for _ in range(k - 1):
            min_data = heappop(min_heap)
            numerator_i = min_data[1]
            denominator_i = min_data[2] - 1

            if denominator_i > numerator_i:
                heappush(min_heap, (
                    arr[numerator_i] / arr[denominator_i],
                    numerator_i,
                    denominator_i
                ))
        k_th_min = heappop(min_heap)

        return [arr[k_th_min[1]], arr[k_th_min[2]]]
