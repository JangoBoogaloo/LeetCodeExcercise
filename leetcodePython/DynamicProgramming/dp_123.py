from typing import List


class SolutionDPMemory:
    @staticmethod
    def _getLeftProfits(prices: List[int]) -> List[int]:
        length = len(prices)
        leftMaxProfitAt = [0] * length
        leftMinPrice = prices[0]
        for day in range(1, length):
            leftMaxProfitAt[day] = max(leftMaxProfitAt[day-1], prices[day] - leftMinPrice)
            leftMinPrice = min(leftMinPrice, prices[day])
        return leftMaxProfitAt

    @staticmethod
    def _getRightProfits(prices: List[int]) -> List[int]:
        length = len(prices)
        rightMaxProfitStartAt = [0] * (length+1)
        rightMaxPrice = prices[-1]
        for day in range(len(prices)-2, -1, -1):
            rightMaxProfitStartAt[day] = max(rightMaxProfitStartAt[day+1], rightMaxPrice - prices[day])
            rightMaxPrice = max(rightMaxPrice, prices[day])
        return rightMaxProfitStartAt

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        leftMaxProfitEndAt = self._getLeftProfits(prices)
        rightMaxProfitStartAt = self._getRightProfits(prices)
        maxProfit = 0
        for day in range(0, len(prices)):
            maxProfit = max(maxProfit, leftMaxProfitEndAt[day] + rightMaxProfitStartAt[day + 1])
        return maxProfit
