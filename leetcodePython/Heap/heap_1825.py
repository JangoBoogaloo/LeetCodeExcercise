from min_max_heap import MinMaxHeap
from collections import deque


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
