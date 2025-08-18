from typing import List


class Solution:
    @staticmethod
    def _getFirstProfits(prices: List[int]) -> List[int]:
        firstProfitSellAt = [0] * len(prices)
        minPrice = prices[0]
        for i in range(1, len(prices)):
            firstProfitSellAt[i] = max(firstProfitSellAt[i-1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return firstProfitSellAt

    @staticmethod
    def _getSecondProfits(prices: List[int]) -> List[int]:
        secondProfitBuyAt = [0] * len(prices)
        maxPrice = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            secondProfitBuyAt[i] = max(secondProfitBuyAt[i+1], maxPrice - prices[i])
            maxPrice = max(maxPrice, prices[i])
        return secondProfitBuyAt

    def maxProfit(self, prices: List[int]) -> int:
        firstProfitSellAt = self._getFirstProfits(prices)
        secondProfitBuyAt = self._getSecondProfits(prices) + [0]
        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, firstProfitSellAt[i] + secondProfitBuyAt[i+1])
        return maxProfit







