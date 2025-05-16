class MyCircularQueue:
    def __init__(self, k: int):
        self._capacity = k
        self._storage = [0] * self._capacity
        self._count = 0
        self._headIndex = 0
        self._tailIndex = -1

    def enQueue(self, value: int) -> bool:
        if self._count == self._capacity:
            return False
        self._storage[(self._headIndex + self._count) % self._capacity] = value
        self._count += 1
        return True

    def deQueue(self) -> bool:
        if self._count == 0:
            return False
        self._headIndex = (self._headIndex + 1) % self._capacity
        self._count -= 1
        return True

    def Front(self) -> int:
        if self._count == 0:
            return -1
        return self._storage[self._headIndex]

    def Rear(self) -> int:
        if self._count == 0:
            return -1
        return self._storage[(self._headIndex + self._count - 1) % self._capacity]

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == self._capacity
