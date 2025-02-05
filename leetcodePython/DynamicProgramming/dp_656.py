from typing import List


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        minCostFrom = [0] * len(coins)
        nextJumpOf = [-1] * len(coins)
        for start in range(len(coins)-2, -1, -1):
            jumpRange = min(start+maxJump+1, len(coins))
            minCost = float("inf")
            for end in range(start+1, jumpRange, 1):
                if coins[end] >= 0:
                    cost = coins[start] + minCostFrom[end]
                    if cost < minCost:
                        minCost = cost
                        nextJumpOf[start] = end
            minCostFrom[start] = minCost

        path = []
        index = 0
        while index < len(coins) and nextJumpOf[index] > 0:
            path.append(index + 1)
            index = nextJumpOf[index]

        if index == len(coins) - 1 and minCostFrom[index] >= 0:
            path.append(len(coins))
            return path

        return []
