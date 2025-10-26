from typing import List
from sortedcontainers import SortedList

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        smallerLeft, smallerRight, biggerLeft, biggerRight = [], [], [], []
        sortedLeft = SortedList()
        sortedRight = SortedList(rating)
        for mid in range(len(rating)):
            sortedRight.remove(rating[mid])
            sortedLeft.add(rating[mid])
            leftSmallerCount = sortedLeft.bisect_left(rating[mid])
            smallerLeft.append(leftSmallerCount)
            leftBiggerCount = mid-leftSmallerCount
            biggerLeft.append(leftBiggerCount)

            rightSmallerCount = sortedRight.bisect_left(rating[mid])
            smallerRight.append(rightSmallerCount)
            rightBiggerCount = len(sortedRight) - rightSmallerCount
            biggerRight.append(rightBiggerCount)

        totalCount = 0
        for mid in range(len(rating)):
            totalCount += smallerLeft[mid] * biggerRight[mid] + biggerLeft[mid] * smallerRight[mid]
        return totalCount









