from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        increaseSubSequence: List[int] = []
        for num in nums:
            numIndex = bisect_left(increaseSubSequence, num)
            if numIndex == len(increaseSubSequence):
                increaseSubSequence.append(num)
            else:
                increaseSubSequence[numIndex] = num
        return len(increaseSubSequence)