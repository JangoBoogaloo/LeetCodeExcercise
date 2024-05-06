class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        for letter in letters:
            left = s.index(letter)
            right = s.rindex(letter)
            between = set()
            for i in range(left + 1, right):
                between.add(s[i])
            ans += len(between)
        return ans
