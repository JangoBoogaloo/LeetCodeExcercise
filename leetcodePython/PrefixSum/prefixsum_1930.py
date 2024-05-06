class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        # kind of O(n^2), but since we only have 26 char, so it is constant for this for loop
        for letter in letters:
            left = s.index(letter)
            right = s.rindex(letter)
            between = set()
            for i in range(left + 1, right):
                between.add(s[i])
            ans += len(between)
        return ans
