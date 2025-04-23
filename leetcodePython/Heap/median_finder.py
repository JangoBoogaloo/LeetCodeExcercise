from collections import defaultdict
from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self._smallHalfMaxHeap = []
        self._largeHalfMinHeap = []
        self._balance = 0
        self._toRemove = defaultdict(int)

    def add(self, num: int) -> None:
        if not self._smallHalfMaxHeap or num <= -self._smallHalfMaxHeap[0]:
            heappush(self._smallHalfMaxHeap, -num)
            self._balance -= 1
        else:
            heappush(self._largeHalfMinHeap, num)
            self._balance += 1
        self._rebalance()

    def remove(self, num:int) ->None:
        self._toRemove[num] += 1
        if num <= -self._smallHalfMaxHeap[0]:
            self._balance += 1
        else:
            self._balance -= 1
        self._rebalance()
        self._lazyRemove()

    def median(self) -> int:
        if self._balance == 0:
            return (-self._smallHalfMaxHeap[0] + self._largeHalfMinHeap[0]) / 2
        elif self._balance < 0:
            return -self._smallHalfMaxHeap[0]
        else:
            return self._largeHalfMinHeap[0]

    def _rebalance(self) -> None:
        while self._balance <0:
            heappush(self._largeHalfMinHeap, -heappop(self._smallHalfMaxHeap))
            self._balance += 2
        while self._balance > 0:
            heappush(self._smallHalfMaxHeap, -heappop(self._largeHalfMinHeap))
            self._balance -= 2
        return

    def _lazyRemove(self):
        while self._smallHalfMaxHeap and self._toRemove[-self._smallHalfMaxHeap[0]] > 0:
            self._toRemove[-self._smallHalfMaxHeap[0]] -= 1
            heappop(self._smallHalfMaxHeap)
        while self._largeHalfMinHeap and self._toRemove[self._largeHalfMinHeap[0]] > 0:
            self._toRemove[self._largeHalfMinHeap[0]] -= 1
            heappop(self._largeHalfMinHeap)
