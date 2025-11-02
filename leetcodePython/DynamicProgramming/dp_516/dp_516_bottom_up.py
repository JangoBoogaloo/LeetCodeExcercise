
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        maxLengthBtw = [[0] * len(s) for _ in range(len(s))]
        for end in range(len(s)):
            maxLengthBtw[end][end] = 1
            for start in range(end-1, -1, -1):
                if s[start] == s[end]:
                    maxLengthBtw[start][end] = maxLengthBtw[start+1][end-1] + 2
                else:
                    maxLengthBtw[start][end] = max(maxLengthBtw[start+1][end], maxLengthBtw[start][end-1])
        return maxLengthBtw[0][-1]








