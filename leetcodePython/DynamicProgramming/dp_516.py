class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        lengthAt = [[0] * len(s) for _ in range(len(s))]
        for right in range(len(s)):
            lengthAt[right][right] = 1
            for left in range(right-1, -1, -1):
                if s[left] == s[right]:
                    lengthAt[left][right] = lengthAt[left + 1][right-1] + 2
                else:
                    lengthAt[left][right] = max(lengthAt[left+1][right], lengthAt[left][right-1])
        return lengthAt[0][len(s)-1]




