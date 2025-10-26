from random import choice

class RandomizedSet:
    def __init__(self):
        self._storage = []
        self._indexOf = {}

    def insert(self, val: int) -> bool:
        if val in self._indexOf:
            return False
        self._indexOf[val] = len(self._storage)
        self._storage.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._indexOf:
            return False
        lastVal = self._storage[len(self._storage) - 1]
        valIndex = self._indexOf[val]
        self._indexOf[lastVal] = valIndex
        del self._indexOf[val]
        self._storage[valIndex], self._storage[-1] = self._storage[-1], self._storage[valIndex]
        self._storage.pop()
        return True

    def getRandom(self) -> int:
        return choice(self._storage)






