from itertools import accumulate
from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0] * (length + 1)
        for start_i, end_i, inc_i in updates:
            nums[start_i] += inc_i
            nums[end_i+1] -= inc_i
        nums = list(accumulate(nums[:-1]))
        return nums
