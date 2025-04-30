class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        subSeqCount = {}
        def countSubseqAt(sIndex: int, tIndex: int) -> int:
            if sIndex == len(s) or tIndex == len(t) or len(s) - sIndex < len(t) - tIndex:
                return int(tIndex == len(t))
            if (sIndex, tIndex) in subSeqCount:
                return subSeqCount[sIndex, tIndex]
            cnt = countSubseqAt(sIndex + 1, tIndex)
            if s[sIndex] == t[tIndex]:
                cnt += countSubseqAt(sIndex + 1, tIndex + 1)
            subSeqCount[sIndex, tIndex] = cnt
            return cnt
        return countSubseqAt(0, 0)
