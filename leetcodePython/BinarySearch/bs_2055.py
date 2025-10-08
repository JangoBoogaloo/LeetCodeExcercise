from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candleIndexes = []
        for i in range(len(s)):
            if s[i] == "|":
                candleIndexes.append(i)
        answer = []
        for left, right in queries:
            l = bisect_left(candleIndexes, left)
            r = bisect_right(candleIndexes, right) - 1
            plates = 0
            if r > l:
                candleCount = r - l
                plateRange = candleIndexes[r] - candleIndexes[l]
                plates = plateRange - candleCount
            answer.append(plates)
        return answer








