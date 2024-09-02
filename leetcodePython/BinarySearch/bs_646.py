from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        prev_right = float('-inf')
        length = 0
        for curr_left, curr_right in pairs:
            if curr_left > prev_right:
                length += 1
                prev_right = curr_right
        return length
