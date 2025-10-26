from typing import List
from collections import Counter


class SolutionSort:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numFreq = Counter(arr)
        frequencies = list(numFreq.values())
        frequencies.sort()
        removals = 0
        for i in range(len(frequencies)):
            removals += frequencies[i]
            if removals > k:
                return len(frequencies) - i
        return 0









