from typing import List


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        minCostToEndFrom = [0] * len(coins)
        INVALID = -1
        bestJumpDstAt = [INVALID] * len(coins)
        for src in range(len(coins)-2, -1, -1):
            dstRange = min(src+maxJump, len(coins)-1)
            minCost = float("inf")
            for dst in range(src+1, dstRange+1):
                if coins[dst] != INVALID:
                    cost = coins[src] + minCostToEndFrom[dst]
                    if cost < minCost:
                        minCost = cost
                        bestJumpDstAt[src] = dst
            minCostToEndFrom[src] = minCost
        path = []
        currentPos = 0
        while currentPos < len(coins) and bestJumpDstAt[currentPos] != INVALID:
            path.append(currentPos)
            currentPos = bestJumpDstAt[currentPos]

        if currentPos == len(coins) - 1 and minCostToEndFrom[currentPos] != INVALID:
            path.append(len(coins)-1)
            # stupid 1-indexed requirement
            return [index+1 for index in path]

        return []
