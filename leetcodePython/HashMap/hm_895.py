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






import pytest

@pytest.mark.parametrize("operations",
[
    ([("push", 1), ("pop", 1)]),
    ([("push", 1), ("push", 1), ("push", 2), ("pop", 1)]),
    ([("push", 1), ("push", 1), ("push", 2), ("pop", 1), ("pop", 2)]),
    ([("pop", None)]),
])
def test_FreqStack(operations):
    freqStack = FreqStack()
    for op in operations:
        match op[0]:
            case "push":
                freqStack.push(op[1])
            case "pop":
                assert freqStack.pop() == op[1]