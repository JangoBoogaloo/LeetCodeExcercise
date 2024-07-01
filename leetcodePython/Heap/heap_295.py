from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self._small_half = []
        self._big_half = []

    def addNum(self, x: int) -> None:
        heappush(self._small_half, -x)
        biggest_small = -heappop(self._small_half)
        heappush(self._big_half, biggest_small)

        if len(self._small_half) < len(self._big_half):
            smallest_big = heappop(self._big_half)
            heappush(self._small_half, -smallest_big)

    def findMedian(self) -> float:
        if len(self._small_half) > len(self._big_half):
            return -self._small_half[0]
        else:
            return (self._big_half[0] - self._small_half[0]) / 2
