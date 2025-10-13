class Solution:
    @staticmethod
    def _expandPalindrome(s:str, left:int, right:int) -> tuple[int, int]:
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        left += 1
        return left, right - left

    def longestPalindrome(self, s: str) -> str:
        maxLength = -1
        maxStart = 0
        for i in range(len(s)):
            start, length = self._expandPalindrome(s, i, i)
            if length > maxLength:
                maxStart, maxLength = start, length
            start, length = self._expandPalindrome(s, i, i+1)
            if length > maxLength:
                maxStart, maxLength = start, length

        return s[maxStart: maxStart+maxLength]
