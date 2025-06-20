from collections import defaultdict, Counter


class UF:
    def __init__(self):
        self._rank = Counter()
        self._parent = defaultdict()
        self._count = 0
        return

    def add(self, data) -> None:
        if self._parent.get(data) is None:
            self._parent[data] = data
            self._count += 1

    def valid(self, data) -> bool:
        return self._parent.get(data) is not None

    def find(self, data):
        if self._parent.get(data) is None:
            raise ValueError(f"data {data} is not added")
        if self._parent.get(data) != data:
            self._parent[data] = self.find(self._parent.get(data))
        return self._parent[data]

    def union(self, data1, data2) -> None:
        data1Root, data2Root = self.find(data1), self.find(data2)
        if data1Root == data2Root:
            return
        if self._rank[data1Root] > self._rank[data2Root]:
            self._parent[data2Root] = data1Root
        elif self._rank[data1Root] < self._rank[data2Root]:
            self._parent[data1Root] = data2Root
        else:
            self._parent[data2Root] = data1Root
            self._rank[data1Root] += 1
        self._count -= 1

    def __len__(self):
        return self._count



class DirectedUF:
    def __init__(self):
        self._rank = Counter()
        self._parent = defaultdict()
        self._count = 0
        return

    def add(self, data) -> None:
        if self._parent.get(data) is None:
            self._parent[data] = data
            self._count += 1

    def valid(self, data) -> bool:
        return self._parent.get(data) is not None

    def find(self, data):
        if self._parent.get(data) is None:
            raise ValueError(f"data {data} is not added")
        if self._parent.get(data) != data:
            self._parent[data] = self.find(self._parent.get(data))
        return self._parent[data]

    def union(self, child, parent) -> None:
        childRoot, parentRoot = self.find(child), self.find(parent)
        if childRoot == parentRoot:
            return
        self._parent[childRoot] = parentRoot
        self._count -= 1

    def __len__(self):
        return self._count