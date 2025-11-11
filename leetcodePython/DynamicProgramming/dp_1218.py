from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dpMaxLengthEndWithNum = {}
        maxLength = 1
        for current in arr:
            previous = current - difference
            prevLength = 0
            if previous in dpMaxLengthEndWithNum:
                prevLength = dpMaxLengthEndWithNum[previous]

            dpMaxLengthEndWithNum[current] = prevLength + 1
            maxLength = max(maxLength, dpMaxLengthEndWithNum[current])

        return maxLength
