import math
from typing import List


class Solution:
    def _can_reach_office(self, dist: List[int], hour: float, speed: float) -> bool:
        spent_hour = 0
        for i in range(len(dist) -1):
            spent_hour += math.ceil(dist[i]/speed)
            if spent_hour > hour:
                return False
        return spent_hour + (dist[-1] / speed) <= hour

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        speed_min = 1
        speed_max = 10**7
        ans = -1
        while speed_min <= speed_max:
            speed_mid = (speed_min + speed_max) // 2
            if self._can_reach_office(dist, hour, speed_mid):
                ans = speed_mid
                speed_max = speed_mid - 1
            else:
                speed_min = speed_mid + 1
        return ans