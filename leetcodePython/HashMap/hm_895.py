from collections import defaultdict
from typing import Optional

class FreqStack:

    def __init__(self):
        self._freqOf = defaultdict(int)
        self._stackOf = defaultdict(list)

    def push(self, val: int) -> None:
        self._freqOf[val] += 1
        self._stackOf[self._freqOf[val]].append(val)

    def pop(self) -> Optional[int]:
        maxFreq = len(self._stackOf)
        if not self._stackOf[maxFreq]:
            return None
        value = self._stackOf[maxFreq].pop()
        self._freqOf[value] -= 1
        if not self._stackOf[maxFreq]:
            del self._stackOf[maxFreq]
        return value






