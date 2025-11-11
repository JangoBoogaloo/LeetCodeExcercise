from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positiveLength, negativeLength = 0, 0
        if nums[0] > 0:
            positiveLength += 1
        elif nums[0] < 0:
            negativeLength += 1
        maxPositiveLength = positiveLength
        for i in range(1, len(nums)):
            if nums[i] > 0:
                positiveLength += 1
                if negativeLength:
                    negativeLength += 1
            elif nums[i] < 0:
                if negativeLength:
                    positiveLength, negativeLength = negativeLength, positiveLength
                    positiveLength += 1
                    negativeLength += 1
                else:
                    negativeLength = 1 + positiveLength
                    positiveLength = 0
            else:
                positiveLength = 0
                negativeLength = 0
            maxPositiveLength = max(maxPositiveLength, positiveLength)
        return maxPositiveLength





