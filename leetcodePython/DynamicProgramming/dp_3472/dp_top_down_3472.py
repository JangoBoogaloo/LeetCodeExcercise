class Solution:
    @staticmethod
    def _opsBtw(ch1, ch2) -> int:
        diff = abs(ord(ch1) - ord(ch2))
        return min(diff, 26 - diff)

    def _subseqLength(self, start, end, ops, s, maxLengthBtwWithOps) -> int:
        # "ac" => 0, 1 => bb
        if start > end:
            return 0
        if start == end:
            return 1
        if maxLengthBtwWithOps[start][end][ops] != -1:
            return maxLengthBtwWithOps[start][end][ops]
        startEndOps = self._opsBtw(s[start], s[end])
        remainOps = ops - startEndOps
        if remainOps >= 0:
            maxLengthBtwWithOps[start][end][ops] = self._subseqLength(start + 1, end - 1, remainOps, s,
                                                                      maxLengthBtwWithOps) + 2
        maxLengthBtwWithOps[start][end][ops] = max(maxLengthBtwWithOps[start][end][ops],
                                                   self._subseqLength(start + 1, end, ops, s, maxLengthBtwWithOps),
                                                    self._subseqLength(start, end - 1, ops, s, maxLengthBtwWithOps))
        return maxLengthBtwWithOps[start][end][ops]

    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        maxLengthBtwWithOps = [[[-1] * (k + 1) for _ in range(len(s))] for _ in range(len(s))]
        return self._subseqLength(0, len(s) - 1, k, s, maxLengthBtwWithOps)







