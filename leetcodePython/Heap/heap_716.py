import heapq


class MaxStack:
    def __init__(self):
        self._removed = set()
        self._stack = []
        self._maxHeap = []
        self._currentId = 0

    def push(self, x: int) -> None:
        self._stack.append((x, self._currentId))
        heapq.heappush(self._maxHeap, (-x, -self._currentId))
        self._currentId += 1

    def pop(self) -> int:
        while self._stack and self._stack[-1][1] in self._removed:
            self._stack.pop()
        num, id = self._stack.pop()
        self._removed.add(id)
        return num

    def top(self) -> int:
        while self._stack and self._stack[-1][1] in self._removed:
            self._stack.pop()
        return self._stack[-1][0]

    def peekMax(self) -> int:
        while self._maxHeap and -self._maxHeap[0][1] in self._removed:
            heapq.heappop(self._maxHeap)
        return -self._maxHeap[0][0]

    def popMax(self) -> int:
        while self._maxHeap and -self._maxHeap[0][1] in self._removed:
            heapq.heappop(self._maxHeap)
        negNum, negId = heapq.heappop(self._maxHeap)
        self._removed.add(-negId)
        return -negNum