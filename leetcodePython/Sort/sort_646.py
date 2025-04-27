from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        prevRight = float('-inf')
        length = 0
        for left, right in pairs:
            if left > prevRight:
                length += 1
                prevRight = right
        return length
