import collections
from heapq import *
from collections import deque


class MinMaxHeap:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self._min_delete = []
        self.max_delete = []
        self.len = 0
        self.sum = 0

    def push(self, val):
        heappush(self.minheap, val)
        heappush(self.maxheap, -val)
        self.len += 1
        self.sum += val

    def pop_min(self):
        self.balance_min()
        val = heappop(self.minheap)

        heappush(self.max_delete, -val)
        self.len -= 1
        self.sum -= val
        return val

    def pop_max(self):
        self.balance_max()
        val = -heappop(self.maxheap)

        heappush(self._min_delete, val)
        self.len -= 1
        self.sum -= val
        return val

    def min(self):
        self.balance_min()
        if len(self.minheap) == 0:
            return 10000000
        return self.minheap[0]

    def max(self):
        self.balance_max()
        if len(self.maxheap) == 0:
            return -10000000
        return -self.maxheap[0]

    def balance_min(self):
        while len(self._min_delete) > 0 and self.minheap[0] == self._min_delete[0]:
            heappop(self._min_delete)
            heappop(self.minheap)

    def balance_max(self):
        while len(self.max_delete) > 0 and self.maxheap[0] == self.max_delete[0]:
            heappop(self.max_delete)
            heappop(self.maxheap)

    def delete(self, val):  # doesn't care if it exits
        heappush(self._min_delete, val)
        heappush(self.max_delete, -val)
        self.len -= 1
        self.sum -= val


class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.ar = deque()
        self.lower_k = MinMaxHeap()
        self.middle = MinMaxHeap()
        self.upper_k = MinMaxHeap()

    def addElement(self, num: int) -> None:
        if len(self.ar) < self.m:
            self.ar.append(num)
            if len(self.ar) == self.m:  # initialize
                sorted_ar = sorted(self.ar)
                for i in range(self.m):
                    if i < self.k:
                        self.lower_k.push(sorted_ar[i])
                    elif i < self.m - self.k:
                        self.middle.push(sorted_ar[i])
                    else:
                        self.upper_k.push(sorted_ar[i])
            return

        # handle ar
        val = self.ar.popleft()
        self.ar.append(num)

        # delete from p1, p2, or p3
        if val <= self.lower_k.max():
            self.lower_k.delete(val)
        elif val <= self.middle.max():
            self.middle.delete(val)
        else:
            self.upper_k.delete(val)

        # push to p1, p2, or p3
        if num < self.lower_k.max():
            self.lower_k.push(num)
        elif num <= self.middle.max():
            self.middle.push(num)
        else:
            self.upper_k.push(num)

        # rebalance
        if self.lower_k.len > self.k:
            self.middle.push(self.lower_k.pop_max())
        if self.upper_k.len > self.k:
            self.middle.push(self.upper_k.pop_min())

        if self.middle.len > self.m - 2 * self.k:
            if self.lower_k.len < self.k:
                self.lower_k.push(self.middle.pop_min())
            if self.upper_k.len < self.k:
                self.upper_k.push(self.middle.pop_max())

    def calculateMKAverage(self) -> int:
        if len(self.ar) < self.m:
            return -1
        return self.middle.sum // self.middle.len
