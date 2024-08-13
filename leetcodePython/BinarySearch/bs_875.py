import math
from typing import List


class Solution:
    @staticmethod
    def _hoursToEatAll(piles: List[int], speed: int) -> int:
        need_hours = 0
        for pile in piles:
            need_hours += math.ceil(pile / speed)
        return need_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower_bound = 1
        upper_bound = max(piles)

        while lower_bound < upper_bound:
            speed_guess = (lower_bound + upper_bound) // 2
            if self._hoursToEatAll(piles, speed_guess) <= h:
                upper_bound = speed_guess
            else:
                lower_bound = speed_guess + 1

        return upper_bound
