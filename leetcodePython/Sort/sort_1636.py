from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numFreq = Counter(nums)
        nums.sort(key=lambda x: (numFreq[x], -x))
        return nums