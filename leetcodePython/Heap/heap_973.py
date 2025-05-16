from typing import List
from math import sqrt
from heapq import *


class SolutionMinHeap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            heappush(min_heap, (sqrt(point[0] * point[0] + point[1] * point[1]), point))

        result = []
        for _ in range(k):
            result.append(heappop(min_heap)[1])
        return result


class SolutionMaxHeap:

    def _sqr_distance(self, point: List[int]) -> float:
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points[:k]):
            heappush(heap, (-self._sqr_distance(point), i))

        for i in range(k, len(points)):
            neg_dist = self._sqr_distance(points[i])
            if neg_dist > heap[0][0]:
                heappushpop(heap, (neg_dist, i))

        return [points[i] for (_, i) in heap]


class SolutionQuickSelect:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, lambda p: p[0] ** 2 + p[1] ** 2)
