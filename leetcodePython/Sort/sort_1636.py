import collections
from functools import cmp_to_key
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = collections.Counter(nums)

        def compare(a: int, b: int) -> int:
            if frequency[a] == frequency[b]:
                return b - a
            return frequency[a] - frequency[b]

        nums.sort(key=cmp_to_key(compare))
        return nums