from typing import *


class MyCircularDeque:

    def __init__(self, k: int):
        self._head, self._tail = Node(), Node()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._count = 0
        self._limit = k

    @staticmethod
    def _insert_between(begin, node, end) -> None:
        begin.next = node
        node.prev = begin
        end.prev = node
        node.next = end

    def insertFront(self, value: int) -> bool:
        if self._count == self._limit:
            return False
        node = Node(value)
        begin = self._head
        end = self._head.next
        self._insert_between(begin, node, end)
        self._count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self._count == self._limit:
            return False
        node = Node(value)
        begin = self._tail.prev
        end = self._tail
        self._insert_between(begin, node, end)
        self._count += 1
        return True

    @staticmethod
    def _delete_between(begin, end) -> None:
        begin.next = end
        end.prev = begin

    def deleteFront(self) -> bool:
        if self._count == 0:
            return False
        begin = self._head
        end = self._head.next.next
        self._delete_between(begin, end)
        self._count -= 1
        return True

    def deleteLast(self) -> bool:
        if self._count == 0:
            return False
        begin = self._tail.prev.prev
        end = self._tail
        self._delete_between(begin, end)
        self._count -= 1
        return True

    def getFront(self) -> int:
        if self._count > 0:
            return self._head.next.value
        return -1

    def getRear(self) -> int:
        if self._count > 0:
            return self._tail.prev.value
        return -1

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == self._limit


class Node:
    def __init__(self, value: Optional[int] = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
