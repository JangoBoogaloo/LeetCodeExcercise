class Solution:
    def minCut(self, s: str) -> int:
        return self._findMinimumCut(0, len(s) - 1, len(s)-1, s)

    def _findMinimumCut(self, start:int, end:int, cuts: int, txt: str) -> int:
        if start == end or self._isPalindrome(start, end, txt):
            return 0

        for i in range(start, end+1):
            if not self._isPalindrome(start, i, txt):
                continue
            cuts = min(cuts, 1+self._findMinimumCut(i+1, end, cuts, txt))
        return cuts

    def _isPalindrome(self, start:int, end:int, txt:str) -> bool:
        while start < end:
            if txt[start] != txt[end]:
                return False
            start += 1
            end -= 1
        return True