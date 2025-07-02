from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i1, i2 = 0, 0
        answer = []
        while i1 < len(firstList) and i2 < len(secondList):
            maxSmall = max(firstList[i1][0], secondList[i2][0])
            minBig = min(firstList[i1][1], secondList[i2][1])
            if maxSmall <= minBig:
                answer.append([maxSmall, minBig])
            if firstList[i1][1] < secondList[i2][1]:
                i1 += 1
            else:
                i2 += 1
        return answer





