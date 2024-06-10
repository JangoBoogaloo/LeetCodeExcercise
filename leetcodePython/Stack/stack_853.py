from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = zip(position, speed)
        time = []
        for p, s in sorted(pos_speed):
            time.append(float(target-p)/s)
        fleets = max_time = 0
        for t in time[::-1]:
            if t > max_time:
                fleets += 1
                max_time = t
        return fleets