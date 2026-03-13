from typing import List


class Solution:
    def _countSubseqAt(self, sIndex, tIndex, s, t, subseqCountAt: List[List[int]]) -> int:
        if tIndex == len(t):
            return 1
        if sIndex == len(s) or len(s) - sIndex < len(t) - tIndex:
            return 0
        if subseqCountAt[sIndex][tIndex] != -1:
            return subseqCountAt[sIndex][tIndex]
        if s[sIndex] != t[tIndex]:
            subseqCountAt[sIndex][tIndex] = self._countSubseqAt(sIndex+1, tIndex, s, t, subseqCountAt)
        else:
            subseqCountAt[sIndex][tIndex] = self._countSubseqAt(sIndex+1, tIndex, s, t, subseqCountAt) + self._countSubseqAt(sIndex+1, tIndex+1, s, t, subseqCountAt)
        return subseqCountAt[sIndex][tIndex]

    def numDistinct(self, s: str, t: str) -> int:
        subseqCountAt = [[-1] * len(t) for _ in range(len(s))]
        return self._countSubseqAt(0, 0, s, t, subseqCountAt)








