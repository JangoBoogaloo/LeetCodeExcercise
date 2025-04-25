from collections import Counter
from math import isqrt
from typing import List


class Solution:
    @staticmethod
    def _carFixCountWithinTime(rank_freq: Counter, time: int) ->int:
        fix_cars = 0
        for rank in rank_freq:
            car_count_sqr = time // rank
            rank_car_count = isqrt(car_count_sqr) * rank_freq[rank]
            fix_cars += rank_car_count
        return fix_cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        rank_freq = Counter(ranks)
        min_rank = min(rank_freq)
        min_time = min_rank
        max_time = min_rank * cars * cars

        while min_time < max_time:
            mid = (min_time + max_time) // 2
            fix_cars = self._carFixCountWithinTime(rank_freq, mid)
            if fix_cars < cars:
                min_time = mid + 1
            else:
                max_time = mid
        return min_time
