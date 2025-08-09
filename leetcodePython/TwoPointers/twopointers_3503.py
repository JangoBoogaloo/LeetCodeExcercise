class Solution:
    @staticmethod
    def _palindromeLength(txt: str, leftCenter: int, rightCenter: int) -> int:
        while leftCenter >= 0 and rightCenter < len(txt) and txt[leftCenter] == txt[rightCenter]:
            leftCenter -= 1
            rightCenter += 1
        return rightCenter - leftCenter - 1

    def longestPalindrome(self, s: str, t: str) -> int:
        maxLength = 0
        for indexS in range(len(s)+1):
            for indexT in range(len(t)+1):
                combined = s[:indexS] + t[indexT:]
                for center in range(len(combined)):
                    len1 = self._palindromeLength(combined, center, center)
                    len2 = self._palindromeLength(combined, center, center+1)
                    maxLength = max(maxLength, len1, len2)
        return maxLength