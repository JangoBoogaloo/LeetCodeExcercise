class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        maxLengthPrevEndStartAt = [0] * len(s)
        maxLengthCurrEndStartAt = [0] * len(s)

        for end in range(len(s)):
            maxLengthCurrEndStartAt[end] = 1
            for start in range(end -1, -1, -1):
                if s[start] == s[end]:
                    maxLengthCurrEndStartAt[start] = maxLengthPrevEndStartAt[start+1] + 2
                else:
                    maxLengthCurrEndStartAt[start] = max(maxLengthPrevEndStartAt[start], maxLengthCurrEndStartAt[start+1])
            maxLengthPrevEndStartAt = maxLengthCurrEndStartAt[:]
        return maxLengthCurrEndStartAt[0]









