
class DNode:
    def __init__(self, value = -1, freq = 1, prev = None, next=None):
        self.value = value
        self.freq = freq
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self._dummyHead = DNode()
        self._dummyTail = DNode()
        self._dummyHead.next = self._dummyTail
        self._dummyTail.prev = self._dummyHead
        self._count = 0

    def appendLeft(self, current: DNode):
        prev = self._dummyHead
        next = self._dummyHead.next
        prev.next = current
        current.prev = prev
        current.next = next
        next.prev = current
        self._count += 1

    def removeNode(self, current: DNode) -> bool:
        if self._count == 0:
            return False
        prev = current.prev
        next = current.next
        prev.next = next
        next.prev = prev
        self._count -= 1
        return True

    def removeLast(self) -> bool:
        if self._count == 0:
            return False
        current = self._dummyTail.prev
        prev = current.prev
        next = self._dummyTail
        current.prev, current.next = None, None
        prev.next = next
        next.prev = prev
        return True


class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._keyValueMap = {}
        self._freqValueMap = {}
        self._count = 0
        self._minAccess = 1

    def get(self, key: int) -> int:
        if key not in self._keyValueMap:
            return -1
        valueNode = self._keyValueMap[key]
        self._updateFrequency(valueNode)
        return valueNode.value

    def _updateFrequency(self, node: DNode) -> None:
        frequency = node.freq
        linklist: LinkedList
        linklist = self._freqValueMap[node.freq]
        linklist.removeNode(node)
        frequency += 1
        if frequency not in self._freqValueMap:
            self._freqValueMap[frequency] = LinkedList()
        self._freqValueMap[frequency].appendLeft(node)

    def put(self, key: int, value: int) -> None:
        if self._count == self._capacity:
