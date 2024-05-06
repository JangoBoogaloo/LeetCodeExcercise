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


class SolutionPrecomputeIndex:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        letter_i = set()
        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            letter_i.add(curr)
            if first[curr] == -1:
                first[curr] = i

            last[curr] = i

        ans = 0
        for i in letter_i:
            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])

            ans += len(between)

        return ans