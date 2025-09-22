from typing import Optional


class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev:Optional[Node] = None
        self.next:Optional[Node] = None
        self.keys = set()

    @staticmethod
    def insert(prev, curr, nxt) -> None:
        prev.next, curr.prev = curr, prev
        curr.next, nxt.prev = nxt, curr

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:
    def __init__(self):
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.keyNodeMap = {}

    def inc(self, key: str) -> None:
        if key in self.keyNodeMap:
            node = self.keyNodeMap[key]
            freq = node.freq
            node.keys.remove(key)
            nextNode = node.next
            if nextNode == self.tail or nextNode.freq != freq + 1:
                newNode = Node(freq + 1)
                newNode.keys.add(key)
                Node.insert(node, newNode, nextNode)
                self.keyNodeMap[key] = newNode
            else:
                nextNode.keys.add(key)
                self.keyNodeMap[key] = nextNode

            if not node.keys:
                node.remove()
        else:
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.freq > 1:
                newNode = Node(1)
                newNode.keys.add(key)
                Node.insert(self.head, newNode, firstNode)
                self.keyNodeMap[key] = newNode
            else:
                firstNode.keys.add(key)
                self.keyNodeMap[key] = firstNode

    def dec(self, key: str) -> None:
        if key not in self.keyNodeMap:
            return  # Key does not exist
        node = self.keyNodeMap[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            del self.keyNodeMap[key]
        else:
            prevNode = node.prev
            if prevNode == self.head or prevNode.freq != freq - 1:
                newNode = Node(freq - 1)
                newNode.keys.add(key)
                Node.insert(prevNode, newNode, node)
                self.keyNodeMap[key] = newNode
            else:
                prevNode.keys.add(key)
                self.keyNodeMap[key] = prevNode
        if not node.keys:
            node.remove()

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""  # No keys exist
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""  # No keys exist
        return next(iter(self.head.next.keys))
