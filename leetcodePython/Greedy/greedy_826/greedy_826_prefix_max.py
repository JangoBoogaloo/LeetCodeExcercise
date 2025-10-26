from typing import List


class Solution:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)
        maxProfitForDifficulty = [0] * (maxAbility + 1)

        for i in range(len(difficulties)):
            difficulty = difficulties[i]
            profit = profits[i]
            if difficulty <= maxAbility:
                maxProfitForDifficulty[difficulty] = max(maxProfitForDifficulty[difficulty], profit)

        for difficulty in range(1, maxAbility + 1):
            maxProfitForDifficulty[difficulty] = max(maxProfitForDifficulty[difficulty], maxProfitForDifficulty[difficulty-1])

        totalProfit = 0
        for difficulty in worker:
            totalProfit += maxProfitForDifficulty[difficulty]
        return totalProfit