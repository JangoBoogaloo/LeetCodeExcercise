from collections import defaultdict
from typing import List


class Solution:
    _maxLength = 1
    def _dfsMaxPath(self, currentIndex:int, childrenIndexOf, s: str):
        currMaxLength = 1
        if not childrenIndexOf[currentIndex]:
            return currMaxLength
        for childIndex in childrenIndexOf[currentIndex]:
            childPathLength = self._dfsMaxPath(childIndex, childrenIndexOf, s)
            if s[childIndex] != s[currentIndex]:
                self._maxLength = max(self._maxLength, childPathLength+currMaxLength)
                currMaxLength = max(currMaxLength, childPathLength+1)
        return currMaxLength

    def longestPath(self, parent: List[int], s: str) -> int:
        childrenIndexOf = defaultdict(list)
        self._maxLength = 1
        for i in range(len(parent)):
            parentIndex = parent[i]
            childrenIndexOf[parentIndex].append(i)
        self._dfsMaxPath(0, childrenIndexOf, s)
        return self._maxLength