from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combinationsFor = [0] * (amount + 1)
        combinationsFor[0] = 1
        for coin in coins:
            for target in range(coin, amount + 1):
                combinationsFor[target] = combinationsFor[target] + combinationsFor[target - coin]
        return combinationsFor[amount]
