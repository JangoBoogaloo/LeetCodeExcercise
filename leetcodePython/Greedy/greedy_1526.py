from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = target[0]
        for i in range(1, len(target)):
            ops += max(0, target[i] - target[i-1])
        return ops








