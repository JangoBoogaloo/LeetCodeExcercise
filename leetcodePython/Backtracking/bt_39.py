from typing import List


class Solution:
    current_sum = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        current = []
        self.current_sum = 0

        def backtrack(index: int):
            if self.current_sum == target:
                combinations.append(current[:])
                return
            if self.current_sum > target:
                return
            for i in range(index, len(candidates)):
                self.current_sum += candidates[i]
                current.append(candidates[i])
                backtrack(i)
                self.current_sum -= candidates[i]
                current.pop()

        backtrack(0)
        return combinations
