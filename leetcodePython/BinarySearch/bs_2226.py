from typing import List


class Solution:
    @staticmethod
    def _childrenWithCandies(candy_piles: List[int], candy_per_child: int) -> int:
        children = 0
        for candies in candy_piles:
            children += candies // candy_per_child
        return children

    def maximumCandies(self, candies: List[int], k: int) -> int:
        lower_bound = 0
        upper_bound = max(candies)
        while lower_bound < upper_bound:
            mid = (lower_bound + upper_bound + 1) // 2
            if self._childrenWithCandies(candies, mid) < k:
                upper_bound = mid - 1
            else:
                lower_bound = mid
        return lower_bound
