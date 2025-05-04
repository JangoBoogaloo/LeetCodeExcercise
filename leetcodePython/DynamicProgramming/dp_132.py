from typing import List, Optional


class Solution:
    def minCut(self, s):
        cutsEndAt = [0] * len(s)
        for i in range(1, len(s)):
            cutsEndAt[i] = i
        for mid in range(len(s)):
            self._findMinimumCuts(mid, mid, cutsEndAt, s)
            self._findMinimumCuts(mid - 1, mid, cutsEndAt, s)
        return cutsEndAt[len(s) - 1]

    @staticmethod
    def _findMinimumCuts(leftCenter, rightCenter, cutsEndAt: List[int], txt: str):
        while leftCenter >= 0 and rightCenter < len(txt) and txt[leftCenter] == txt[rightCenter]:
            if leftCenter == 0:
                newCut = 0
            else:
                newCut = cutsEndAt[leftCenter - 1] + 1
            cutsEndAt[rightCenter] = min(cutsEndAt[rightCenter], newCut)
            leftCenter -= 1
            rightCenter += 1




