from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current = []
        combinations = []

        def backtrack(start: int):
            if len(current) == k:
                combinations.append(list(current))
                return
            for num in range(start, n + 1):
                current.append(num)
                backtrack(num + 1)
                current.pop()

        backtrack(1)

        return combinations