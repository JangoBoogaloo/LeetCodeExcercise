from typing import List


class Solution:
    def _countSubSeqAt(self, sIndex: int, s: str, tIndex: int, t: str, subSeqCountAt: List[List[int]]) -> int:
        if sIndex == len(s) or tIndex == len(t) or len(s) - sIndex < len(t) - tIndex:
            return int(tIndex == len(t))
        if subSeqCountAt[sIndex][tIndex] != -1:
            return subSeqCountAt[sIndex][tIndex]
        count = self._countSubSeqAt(sIndex + 1, s, tIndex, t, subSeqCountAt)
        if s[sIndex] == t[tIndex]:
            count = count + self._countSubSeqAt(sIndex + 1, s, tIndex + 1, t, subSeqCountAt)
        subSeqCountAt[sIndex][tIndex] = count
        return count

    def numDistinct(self, s: str, t: str) -> int:
        subSeqCountAt =[[-1] * len(t) for _ in range(len(s))]
        return self._countSubSeqAt(0, s, 0, t, subSeqCountAt)






