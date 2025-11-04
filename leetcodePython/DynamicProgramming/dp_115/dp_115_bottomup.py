class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        subseqWithCount = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for sCount in range(len(s)+1):
            subseqWithCount[sCount][0] = 1

        for sCount in range(1, len(s)+1):
            for tCount in range(1, len(t) + 1):
                sIndex, tIndex = sCount - 1, tCount - 1
                if s[sIndex] == t[tIndex]:
                    subseqWithCount[sCount][tCount] = subseqWithCount[sCount-1][tCount-1] + subseqWithCount[sCount-1][tCount]
                else:
                    subseqWithCount[sCount][tCount] = subseqWithCount[sCount-1][tCount]
        return subseqWithCount[-1][-1]






