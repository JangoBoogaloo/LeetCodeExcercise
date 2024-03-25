class Solution:
    def checkPalindrome(self, s: str, left: int, right: int) -> bool:
        if left < 0 or right > len(s)-1:
            return False
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.checkPalindrome(s, left+1, right) or self.checkPalindrome(s, left, right-1)
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.validPalindrome("abcdba"))