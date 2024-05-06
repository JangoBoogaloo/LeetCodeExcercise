import string


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


class SolutionClean:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1: j]))
        return res