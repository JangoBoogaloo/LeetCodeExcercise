from typing import Optional


class DNode:
    def __init__(self, key= -1, value=-1, freq=-1, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = prev
        self.next = nxt


class LinkedList:
    def __init__(self):
        self._dummyHead = DNode()
        self._dummyTail = DNode()
        self._dummyHead.next = self._dummyTail
        self._dummyTail.prev = self._dummyHead
        self._count = 0

    def appendLeft(self, current: DNode):
        prev, nxt = self._dummyHead, self._dummyHead.next
        prev.next, current.prev = current, prev
        nxt.prev, current.next = current, nxt
        self._count += 1

    def remove(self, current: DNode) -> bool:
        if self._count == 0:
            return False
        prev, nxt = current.prev, current.next
        prev.next, nxt.prev = nxt, prev
        self._count -= 1
        return True

    def last(self) -> Optional[DNode]:
        if self._count == 0:
            return None
        return self._dummyTail.prev

    def count(self) -> int:
        return self._count

class LFUCache:
    def __init__(self, capacity: int):
        self._freqLinkedListMap = {}
        self._keyNodeMap = {}
        self._capacity = capacity
        self._cacheSize = 0
        self._minFrequency = 1

    def get(self, key: int) -> int:
        if key not in self._keyNodeMap:
            return -1
        node = self._keyNodeMap[key]
        self._updateFrequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self._keyNodeMap:
            node = self._keyNodeMap[key]
            node.value = value
            self._updateFrequency(node)
            return
        if self._cacheSize == self._capacity:
            self._removeLeastFrequentLeastRecent()

        node = DNode(key, value, 1)
        self._keyNodeMap[key] = node
        if node.freq not in self._freqLinkedListMap:
            self._freqLinkedListMap[node.freq] = LinkedList()
            if node.freq < self._minFrequency:
                self._minFrequency = node.freq
        self._freqLinkedListMap[node.freq].appendLeft(node)
        self._cacheSize += 1

    def _updateFrequency(self, node: DNode) -> None:
        linkedlist: LinkedList = self._freqLinkedListMap[node.freq]
        linkedlist.remove(node)
        if self._minFrequency == node.freq and linkedlist.count() == 0:
            self._freqLinkedListMap.pop(node.freq)
            self._minFrequency += 1
        node.freq += 1
        if node.freq not in self._freqLinkedListMap:
            self._freqLinkedListMap[node.freq] = LinkedList()
        self._freqLinkedListMap[node.freq].appendLeft(node)

    def _removeLeastFrequentLeastRecent(self) -> None:
        leastFreqList = self._freqLinkedListMap[self._minFrequency]
        last = leastFreqList.last()
        if last:
            leastFreqList.remove(last)
            self._keyNodeMap.pop(last.key)
        if leastFreqList.count() == 0:
            self._freqLinkedListMap.pop(self._minFrequency)
        self._cacheSize -= 1