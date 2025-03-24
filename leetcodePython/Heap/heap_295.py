from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self._smallHalfMaxHeap = []
        self._bigHalfMinHeap = []
        return

    def addNum(self, x: int) -> None:
        heappush(self._bigHalfMinHeap, x)
        smallestBigHalf = heappop(self._bigHalfMinHeap)
        heappush(self._smallHalfMaxHeap, -smallestBigHalf)
        if len(self._smallHalfMaxHeap) > len(self._bigHalfMinHeap):
            biggestSmallHalf = -heappop(self._smallHalfMaxHeap)
            heappush(self._bigHalfMinHeap, biggestSmallHalf)
        return

    def findMedian(self) -> float:
        if len(self._bigHalfMinHeap) > len(self._smallHalfMaxHeap):
            return self._bigHalfMinHeap[0]
        return (self._bigHalfMinHeap[0] - self._smallHalfMaxHeap[0]) / 2
