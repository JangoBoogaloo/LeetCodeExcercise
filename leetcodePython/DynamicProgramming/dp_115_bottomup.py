class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        subSeqCountEndAt = [[0] * (len(t) + 1) for _ in range(len(s)+1)]
        for sIndex in range(len(s)+1):
            subSeqCountEndAt[sIndex][0] = 1

        for sIndex in range(1, len(s)+1):
            for tIndex in range(1, len(t) + 1):
                subSeqCountEndAt[sIndex][tIndex] += subSeqCountEndAt[sIndex-1][tIndex]
                if s[sIndex-1] == t[tIndex-1]:
                    subSeqCountEndAt[sIndex][tIndex] += subSeqCountEndAt[sIndex-1][tIndex-1]
        return subSeqCountEndAt[-1][-1]






