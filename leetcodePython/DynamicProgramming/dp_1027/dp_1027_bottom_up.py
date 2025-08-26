from collections import defaultdict
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        lengthEndAtIndexWithDiff = [defaultdict(int) for _ in range(len(nums))]
        maxLength = 0
        for endIndex in range(len(nums)):
            for i in range(endIndex):
                diff = nums[i] - nums[endIndex]
                lengthEndAtIndexWithDiff[endIndex][diff] = 1 + lengthEndAtIndexWithDiff[i][diff]
                maxLength = max(maxLength, lengthEndAtIndexWithDiff[endIndex][diff])
        return maxLength + 1