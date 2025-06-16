from collections import defaultdict
from typing import List


class Solution:
    _maxLength = 1
    def _dfsMaxPath(self, currentIndex:int, childrenIndexOf, s: str):
        currLength = 1
        if not childrenIndexOf[currentIndex]:
            return currLength
        for childIndex in childrenIndexOf[currentIndex]:
            childLength = self._dfsMaxPath(childIndex, childrenIndexOf, s)
            if s[childIndex] != s[currentIndex]:
                self._maxLength = max(self._maxLength, childLength+currLength)
                currLength = max(currLength, childLength+1)
        return currLength

    def longestPath(self, parent: List[int], s: str) -> int:
        childrenIndexOf = defaultdict(list)
        self._maxLength = 1
        for i in range(len(parent)):
            parentIndex = parent[i]
            childrenIndexOf[parentIndex].append(i)
        self._dfsMaxPath(0, childrenIndexOf, s)
        return self._maxLength