from typing import List


class SolutionBacktrack:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balanceMap = {}
        for from_i, to_i, amount_i in transactions:
            if from_i not in balanceMap:
                balanceMap[from_i] = 0
            balanceMap[from_i] -= amount_i
            if to_i not in balanceMap:
                balanceMap[to_i] = 0
            balanceMap[to_i] += amount_i

        userBalances = list(balanceMap.values())

        def minOperationsAt(index: int) -> int:
            while index < len(userBalances) and userBalances[index] == 0:
                index += 1
            if index == len(userBalances):
                return 0
            cost = float("inf")
            for next_i in range(index+1, len(userBalances)):
                if userBalances[next_i] * userBalances[index] >= 0:
                    continue
                userBalances[next_i] += userBalances[index]
                currentCost = 1 + minOperationsAt(index+1)
                cost = min(cost, currentCost)
                userBalances[next_i] -= userBalances[index]
            return cost

        return minOperationsAt(0)
