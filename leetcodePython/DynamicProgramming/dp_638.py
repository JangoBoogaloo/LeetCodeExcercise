from functools import cache
from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @cache
        def minCostForNeed(currNeeds: tuple) -> int:
            cost = sum(need * price[i] for i, need in enumerate(currNeeds))
            for offer in special:
                nextNeed = [currNeeds[i] - offer[i] for i in range(len(needs))]
                if min(nextNeed) < 0:
                    continue
                cost = min(cost, offer[-1] + minCostForNeed(tuple(nextNeed)))
            return cost

        return minCostForNeed(tuple(needs))







