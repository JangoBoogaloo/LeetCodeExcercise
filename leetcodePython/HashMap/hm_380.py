from random import choice
from typing import List

class RandomizedSet:

    def __init__(self):
        self._storage = []
        self._dict = {}

    def insert(self, val: int) -> bool:
        if val in self._dict:
            return False
        self._dict[val] = len(self._storage)
        self._storage.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._dict:
            return False
        lastIndex = len(self._storage) - 1
        valIndex = self._dict[val]
        self._dict[self._storage[lastIndex]] = valIndex
        del self._dict[val]
        self._removeAtIndex(valIndex, self._storage)
        return True

    @staticmethod
    def _removeAtIndex(index: int, nums: List[int]):
        nums[index], nums[-1] = nums[-1], nums[index]
        nums.pop()

    def getRandom(self) -> int:
        return choice(self._storage)






