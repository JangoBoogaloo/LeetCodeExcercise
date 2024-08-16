import heapq
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
        base_price = right
        while left < right:
            base_price = (left + right) // 2
            if self._sold_balls(inventory, base_price) > orders:
                left = base_price + 1
            else:
                right = base_price

        sold_balls = 0
        total = 0
        for price in inventory:
            if price > right:
                sold_balls += price - right
                bigger_price_sum = (price + right + 1) * (price - right) // 2
                total += bigger_price_sum

        if sold_balls < orders:
            total += (orders - sold_balls) * right
        return total % 1_000_000_007
