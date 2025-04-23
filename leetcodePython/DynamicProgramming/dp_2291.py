from typing import List


class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        maxProfitWith = [0] * (budget + 1)
        for p, f in zip(present, future):
            if f < p:
                continue
            for currentBudget in range(budget, p-1, -1):
                maxProfitWith[currentBudget] = max(maxProfitWith[currentBudget], maxProfitWith[currentBudget-p] + f - p)
        return maxProfitWith[-1]
