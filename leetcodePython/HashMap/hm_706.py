class Node:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

    def get(self, key:int) -> int:
        head = self.next
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def update(self, key:int, value:int):
        head = self.next
        tail = self
        while head:
            if head.key == key:
                head.value = value
                return
            tail = head
            head = head.next
        tail.next = Node(key, value)

    def remove(self, key: int):
        prev = self
        current = self.next
        while current:
            if current.key == key:
                #prev->current->next
                #prev->next
                prev.next = current.next
                return
            prev = current
            current = current.next


class MyHashMap:
    def __init__(self):
        self._key_space = 2069
        self._table = [Node() for _ in range(self._key_space)]

    def put(self, key: int, value: int) -> None:
        table_index = key % self._key_space
        self._table[table_index].update(key, value)

    def get(self, key: int) -> int:
        table_index = key % self._key_space
        return self._table[table_index].get(key)

    def remove(self, key: int) -> None:
        table_index = key % self._key_space
        self._table[table_index].remove(key)