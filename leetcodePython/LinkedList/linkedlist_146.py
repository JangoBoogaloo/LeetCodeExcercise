class DNode:
    def __init__(self, key: int, value: int, prev=None, next=None):
        self.prev = prev
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self._key_node_map = {}
        self._capacity = capacity
        self._dummy_head = DNode(-1, -1)
        self._dummy_tail = DNode(-1, -1)
        self._dummy_head.next = self._dummy_tail
        self._dummy_tail.prev = self._dummy_head

    def _remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node) -> None:
        # prev <-> key_node <-> _dummy_tail
        prev = self._dummy_tail.prev
        prev.next = node
        node.prev = prev
        node.next = self._dummy_tail
        self._dummy_tail.prev = node

    def get(self, key: int) -> int:
        if key not in self._key_node_map:
            return -1
        key_node = self._key_node_map[key]
        self._remove(key_node)
        self._append(key_node)
        return key_node.value

    def put(self, key: int, value: int) -> None:
        if key in self._key_node_map:
            old_node = self._key_node_map[key]
            self._remove(old_node)
        node = DNode(key, value)
        self._key_node_map[key] = node
        self._append(node)
        if len(self._key_node_map) > self._capacity:
            to_delete = self._dummy_head.next
            self._remove(to_delete)
            self._key_node_map.pop(to_delete.key, None)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))
    cache.put(4,4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))