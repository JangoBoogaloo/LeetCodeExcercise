class Solution:
    @staticmethod
    def _expandFrom(leftCutStartIndex, rightEndindex, minCutsEndAt, txt: str):
        while leftCutStartIndex >=0 and rightEndindex < len(txt) and txt[leftCutStartIndex] == txt[rightEndindex]:
            cuts = 0
            if leftCutStartIndex:
                cuts = minCutsEndAt[leftCutStartIndex-1] + 1
            minCutsEndAt[rightEndindex] = min(minCutsEndAt[rightEndindex], cuts)
            leftCutStartIndex -= 1
            rightEndindex += 1

    def minCut(self, s: str) -> int:
        minCutsEndAt = [i for i in range(len(s))]
        for midPos in range(len(s)):
            self._expandFrom(midPos, midPos, minCutsEndAt, s)
            self._expandFrom(midPos, midPos+1, minCutsEndAt, s)
        return minCutsEndAt[-1]





