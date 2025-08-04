class Solution:
    def minInsertions(self, s: str) -> int:
        longestCommonEndAt = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        for i1 in range(1, len(s)+1):
            for i2 in range(1, len(s)+1):
                if s[i1-1] == s[len(s) - i2]:
                    longestCommonEndAt[i1][i2] = 1 + longestCommonEndAt[i1-1][i2-1]
                else:
                    longestCommonEndAt[i1][i2] = max(longestCommonEndAt[i1-1][i2], longestCommonEndAt[i1][i2-1])
        return len(s) - longestCommonEndAt[-1][-1]





