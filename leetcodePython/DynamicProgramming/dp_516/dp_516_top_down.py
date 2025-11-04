class Solution:
    def _maxPalBtw(self, left, right, txt: str, maxLengthBtw) -> int:
        if left > right:
            return 0
        if left == right:
            return 1
        if maxLengthBtw[left][right] != 0:
            return maxLengthBtw[left][right]
        maxLength = 1
        if txt[left] == txt[right]:
            maxLength = 2 + self._maxPalBtw(left + 1, right - 1, txt, maxLengthBtw)
        else:
            maxLength = max(self._maxPalBtw(left + 1, right, txt, maxLengthBtw), self._maxPalBtw(left, right - 1, txt, maxLengthBtw))
        maxLengthBtw[left][right] = maxLength
        return maxLengthBtw[left][right]

    def longestPalindromeSubseq(self, s: str) -> int:
        maxLengthBtw = [[0] * len(s) for _ in range(len(s))]
        ans = self._maxPalBtw(0, len(s) - 1, s, maxLengthBtw)
        return ans







