from typing import List


class Solution:
    # if we set a base_price, how many balls can we sell with more than this price
    # get maximum price (and maximum balls sold) will be our greedy strategy
    @staticmethod
    def _sold_balls(inventory: List[int], base_price: int) -> int:
        balls = 0
        for price in inventory:
            if price > base_price:
                balls += (price - base_price)
        return balls

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        left, right = 0, max(inventory)
        basePrice = right
        while left < right:
            guess = (left + right) // 2
            if self._sold_balls(inventory, guess) > orders:
                left = guess + 1
            else:
                right = guess
                basePrice = guess

        soldBalls = 0
        total = 0
        for price in inventory:
            if price > basePrice:
                soldBalls += price - basePrice
                biggerPriceSum = (price + basePrice + 1) * (price - basePrice) // 2
                total += biggerPriceSum

        if soldBalls < orders:
            total += (orders - soldBalls) * basePrice
        return total % 1_000_000_007
