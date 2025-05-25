class Solution:
    def maxScore(self, s: str) -> int:
        oneSum = s.count('1')
        zeroSum = 0
        score = 0
        for split in range(len(s)-1):
            if s[split] == '1':
                oneSum -= 1
            else:
                zeroSum += 1
            score = max(score, zeroSum+oneSum)
        return score
