class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longestSubEndAt = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)]
        for i1 in reversed(range(len(text1))):
            for i2 in reversed(range(len(text2))):
                if text1[i1] == text2[i2]:
                    longestSubEndAt[i1][i2] = 1 + longestSubEndAt[i1+1][i2+1]
                else:
                    longestSubEndAt[i1][i2] = max(longestSubEndAt[i1+1][i2], longestSubEndAt[i1][i2+1])
        return longestSubEndAt[0][0]






