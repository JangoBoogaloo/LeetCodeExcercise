from typing import List
from heapq import *

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)-{0})