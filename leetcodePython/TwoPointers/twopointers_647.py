class Solution:
    @staticmethod
    def _countPalindromeFromCenter(s:str, leftCenter, rightCenter) -> int:
        count = 0
        while leftCenter > -1 and rightCenter < len(s):
            if s[leftCenter] != s[rightCenter]:
                break
            leftCenter -= 1
            rightCenter += 1
            count += 1
        return count

    def countSubstrings(self, s: str) -> int:
        palindromeCount = 0
        for i in range(len(s)):
            palindromeCount += self._countPalindromeFromCenter(s, i, i)
            palindromeCount += self._countPalindromeFromCenter(s, i, i+1)
        return palindromeCount