class Solution:
    @staticmethod
    def _opsBtw(ch1, ch2) -> int:
        diff = abs(ord(ch1) - ord(ch2))
        return min(diff, 26 - diff)

    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        maxLengthBtwWithOps = [[[0] * (k + 1) for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for ops in range(k + 1):
                maxLengthBtwWithOps[i][i][ops] = 1

        for ops in range(k+1):
            for end in range(1, len(s)):
                for start in range(end-1, -1, -1):
                    startEndOps = self._opsBtw(s[start], s[end])
                    remainOps = ops - startEndOps
                    if remainOps >= 0:
                        maxLengthBtwWithOps[start][end][ops] = maxLengthBtwWithOps[start+1][end-1][remainOps] + 2
                    maxLengthBtwWithOps[start][end][ops] = max(maxLengthBtwWithOps[start][end][ops],
                                                               maxLengthBtwWithOps[start+1][end][ops],
                                                               maxLengthBtwWithOps[start][end-1][ops])
        return maxLengthBtwWithOps[0][-1][k]









