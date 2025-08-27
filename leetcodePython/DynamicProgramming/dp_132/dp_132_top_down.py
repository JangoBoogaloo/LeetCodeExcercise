class Solution:
    def _isPalindrome(self, start, end, txt:str, isPalindrome) -> bool:
        if start >= end:
            return True
        if isPalindrome[start][end] is not None:
            return isPalindrome[start][end]
        if txt[start] != txt[end]:
            return False
        return self._isPalindrome(start+1, end-1, txt, isPalindrome)

    def _minCutBetween(self, start, end, minCuts, txt:str, isPalindrome, cutsFor) -> int:
        if start == end or self._isPalindrome(start, end, isPalindrome):
            return 0
        if cutsFor[start][end] is not None:
            return cutsFor[start][end]
        for cutEndIndex in range(start, end + 1):
            if self._isPalindrome(start, cutEndIndex, isPalindrome):
                minCuts = min(minCuts, 1 + self._minCutBetween(cutEndIndex+1, end, txt, minCuts, isPalindrome, cutsFor))
        cutsFor[start][end] = minCuts
        return cutsFor[start][end]

    def minCut(self, s: str) -> int:
        isPalindrome = [[None] * len(s) for _ in range(len(s))]
        cutsFor = [[None] * len(s) for _ in range(len(s))]
        return self._minCutBetween(0, len(s)-1, len(s)-1, s, isPalindrome, cutsFor)







