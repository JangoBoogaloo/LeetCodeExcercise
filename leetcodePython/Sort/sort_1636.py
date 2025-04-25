import collections
from functools import cmp_to_key
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = collections.Counter(nums)
        return sorted(nums, key=lambda x: (frequency[x], -x))