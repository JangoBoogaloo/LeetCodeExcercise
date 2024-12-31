from itertools import accumulate
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self._sums = [0]+list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self._sums[right+1] - self._sums[left]
