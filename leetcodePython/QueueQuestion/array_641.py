class MyCircularDeque:
    def __init__(self, k: int) -> None:
        self._capacity = k
        self._storage = [0] * self._capacity
        self._count = 0
        self._headIndex = 0

    def insertFront(self, value: int) -> bool:
        if self._count == self._capacity:
            return False
        self._headIndex = (self._headIndex - 1 + self._capacity) % self._capacity
        self._storage[self._headIndex] = value
        self._count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self._count == self._capacity:
            return False
        # [1, _, _.....]
        # [1, 2, _, ....]
        insertIndex = (self._headIndex + self._count) % self._capacity
        self._storage[insertIndex] = value
        self._count += 1
        return True

    def deleteFront(self) -> bool:
        if self._count == 0:
            return False
        self._headIndex = (self._headIndex + 1) % self._capacity
        self._count -= 1
        return True

    def deleteLast(self) -> bool:
        if self._count == 0:
            return False
        self._count -= 1
        return True

    def getFront(self) -> int:
        if self._count == 0:
            return -1
        return self._storage[self._headIndex]

    def getRear(self) -> int:
        if self._count == 0:
            return -1
        tailIndex = (self._headIndex + self._count - 1) % self._capacity
        return self._storage[tailIndex]

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == self._capacity
