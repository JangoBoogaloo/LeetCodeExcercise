from random import uniform
from typing import List
from bisect import bisect_left


class Solution:
    def __init__(self, w: List[int]):
        sum_w = sum(w)
        run_sum = 0
        self._prefix_probs = []
        for num in w:
            run_sum += num / sum_w
            self._prefix_probs.append(run_sum)
        print(self._prefix_probs)

    def pickIndex(self) -> int:
        p = uniform(0, 1)
        i = bisect_left(self._prefix_probs, p)
        return i