import math
from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        loc_points = 0
        points_in_radian = []
        for x, y in points:
            if x == location[0] and y == location[1]:
                loc_points += 1
                continue
            points_in_radian.append(math.atan2(y-location[1], x-location[0]))

        points_in_radian.sort()
        # why do we need `circular array`? because we can make 360 rotation, and that will loop back to count the beginning points
        points_in_radian = points_in_radian + [radian + 2.0*math.pi for radian in points_in_radian]
        angle_in_radian = math.pi * angle / 180

        left = 0
        max_points_in_fov = 0
        for right in range(len(points_in_radian)):
            while points_in_radian[right] - points_in_radian[left] > angle_in_radian:
                left += 1
            max_points_in_fov = max(max_points_in_fov, right - left + 1)
        return max_points_in_fov + loc_points
