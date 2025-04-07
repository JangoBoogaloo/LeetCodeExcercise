from heapq import heappop, heappush


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
        self._balance_min()
        val = heappop(self.minheap)

        heappush(self.max_delete, -val)
        self.len -= 1
        self.sum -= val
        return val

    def pop_max(self):
        self._balance_max()
        val = -heappop(self.maxheap)

        heappush(self._min_delete, val)
        self.len -= 1
        self.sum -= val
        return val

    def min(self):
        self._balance_min()
        if len(self.minheap) == 0:
            return 10000000
        return self.minheap[0]

    def max(self):
        self._balance_max()
        if len(self.maxheap) == 0:
            return -10000000
        return -self.maxheap[0]

    def delete(self, val):  # doesn't care if it exits
        heappush(self._min_delete, val)
        heappush(self.max_delete, -val)
        self.len -= 1
        self.sum -= val

    def _balance_min(self):
        while len(self._min_delete) > 0 and self.minheap[0] == self._min_delete[0]:
            heappop(self._min_delete)
            heappop(self.minheap)

    def _balance_max(self):
        while len(self.max_delete) > 0 and self.maxheap[0] == self.max_delete[0]:
            heappop(self.max_delete)
            heappop(self.maxheap)
