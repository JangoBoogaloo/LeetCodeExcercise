from typing import List


class Solution:
    current_sum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        current = []
        self.current_sum = 0
        candidates.sort()

        def backtrack(index: int) -> None:
            if self.current_sum == target:
                combinations.append(current[:])
                return
            if self.current_sum > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                self.current_sum += candidates[i]
                current.append(candidates[i])
                backtrack(i + 1)
                self.current_sum -= candidates[i]
                current.pop()

        backtrack(0)
        return combinations
