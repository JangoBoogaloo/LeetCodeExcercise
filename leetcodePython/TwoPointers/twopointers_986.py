from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_i, second_j = 0, 0
        ans = []
        while first_i < len(firstList) and second_j < len(secondList):
            max_small = max(firstList[first_i][0], secondList[second_j][0])
            min_big = min(firstList[first_i][1], secondList[second_j][1])
            if max_small <= min_big:
                ans.append([max_small, min_big])

            if firstList[first_i][1] < secondList[second_j][1]:
                first_i += 1
            else:
                second_j += 1
        return ans