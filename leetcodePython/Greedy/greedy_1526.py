from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = target[0]
        for i in range(1, len(target)):
            ops += max(0, target[i] - target[i-1])
        return ops


class SolutionMonotonicStack:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = 0
        decreaseHeightAndOps = [(0, 0)]
        for height in target:
            ops = max(0, height - decreaseHeightAndOps[-1][0])
            while decreaseHeightAndOps and height > decreaseHeightAndOps[-1][0]:
                _, prevOps = decreaseHeightAndOps.pop()
                operations += prevOps
            decreaseHeightAndOps.append((height, ops))

        while decreaseHeightAndOps:
            operations += decreaseHeightAndOps.pop()[1]
        return operations
