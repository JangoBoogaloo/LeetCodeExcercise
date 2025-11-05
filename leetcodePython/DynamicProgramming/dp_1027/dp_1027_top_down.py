from collections import defaultdict
from typing import List


class Solution:
    def _lengthStartAt(self, startIndex:int, diff, nums: List[int], lengthStartAtIndexWithDiff) -> int:
        if startIndex == len(nums):
            return 0
        if startIndex in lengthStartAtIndexWithDiff:
            return lengthStartAtIndexWithDiff[startIndex][diff]
        for i in range(startIndex + 1, len(nums)):
            newDiff = nums[i] - nums[startIndex]
            lengthStartAtIndexWithDiff[startIndex][newDiff] = max(lengthStartAtIndexWithDiff[startIndex][newDiff], 1 + self._lengthStartAt(i, newDiff, nums, lengthStartAtIndexWithDiff))
            self._maxLength = max(self._maxLength, lengthStartAtIndexWithDiff[startIndex][newDiff])
        return lengthStartAtIndexWithDiff[startIndex][diff]

    def longestArithSeqLength(self, nums: List[int]) -> int:
        self._maxLength = 0
        lengthStartAtIndexWithDiff = defaultdict(lambda: defaultdict(lambda: 1))
        self._lengthStartAt(0, None, nums, lengthStartAtIndexWithDiff)
        return self._maxLength