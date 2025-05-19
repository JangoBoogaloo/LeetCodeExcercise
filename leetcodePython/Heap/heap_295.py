from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self._smallHalfMaxHeap = []
        self._bigHalfExtraMinHeap = []
        return

    def addNum(self, x: int) -> None:
        heappush(self._bigHalfExtraMinHeap, x)
        smallestBigHalf = heappop(self._bigHalfExtraMinHeap)
        heappush(self._smallHalfMaxHeap, -smallestBigHalf)
        if len(self._smallHalfMaxHeap) > len(self._bigHalfExtraMinHeap):
            biggestSmallHalf = -heappop(self._smallHalfMaxHeap)
            heappush(self._bigHalfExtraMinHeap, biggestSmallHalf)
        return

    def findMedian(self) -> float:
        if len(self._bigHalfExtraMinHeap) > len(self._smallHalfMaxHeap):
            return self._bigHalfExtraMinHeap[0]
        return (self._bigHalfExtraMinHeap[0] - self._smallHalfMaxHeap[0]) / 2
