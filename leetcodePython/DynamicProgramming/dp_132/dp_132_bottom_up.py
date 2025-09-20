from typing import List


class Solution:
    def _isPalindrome(self, start:int, end:int, txt:str, isPalindrome) -> bool:
        if start >= end:
            return True
        if isPalindrome[start][end] is not None:
            return isPalindrome[start][end]
        if txt[start] != txt[end]:
            isPalindrome[start][end] = False
            return isPalindrome[start][end]
        isPalindrome[start][end] = self._isPalindrome(start+1, end-1, txt, isPalindrome)
        return isPalindrome[start][end]

    def _palindromeStatus(self, txt:str) -> List[List[bool]]:
        isPalindromeBtw = [[False] * len(txt) for _ in range(len(txt))]
        for end in range(len(txt)):
            for start in range(end+1):
                if txt[start] != txt[end]:
                    continue
                if end - start <= 2:
                    isPalindromeBtw[start][end] = True
                    continue
                isPalindromeBtw[start][end] = isPalindromeBtw[start+1][end-1]
        return isPalindromeBtw

    def minCut(self, s: str) -> int:
        isPalindromeBtw = self._palindromeStatus(s)
        cutsAt = [0] * len(s)
        for end in range(len(s)):
            minCut = end
            for cutStart in range(end + 1):
                if isPalindromeBtw[cutStart][end]:
                    if cutStart == 0:
                        minCut = 0
                    else:
                        minCut = min(minCut, cutsAt[cutStart-1]+1)
            cutsAt[end] = minCut
        return cutsAt[-1]





