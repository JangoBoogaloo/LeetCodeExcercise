class Solution:
    @staticmethod
    def _validPalindrome(s:str, left:int, right:int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self._validPalindrome(s, left+1, right) or self._validPalindrome(s, left, right-1)
            left += 1
            right -= 1
        return True