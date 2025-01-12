class Node:
    def __init__(self, value=-1, next=None)->None:
        self.value = value
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self._head = None
        self._tail = None
        self._capacity = k
        self._count = 0

    def enQueue(self, value: int) -> bool:
        if self._count == self._capacity:
            return False
        if self._count == 0:
            self._head = Node(value)
            self._tail = self._head
            self._head.next = self._head
            self._count += 1
            return True
        # tail -> head
        # tail -> node -> head
        self._tail.next = Node(value, self._head)
        self._tail = self._tail.next
        self._count += 1

    def deQueue(self) -> bool:
        if self._count == 0:
            return False
        # tail->head->next
        # tail->next
        self._tail.next = self._head.next
        self._head = self._head.next
        self._count -= 1
        return True

    def Front(self) -> int:
        if self._count == 0:
            return -1
        return self._head.value

    def Rear(self) -> int:
        if self._count == 0:
            return -1
        return self._tail.value

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == self._capacity
