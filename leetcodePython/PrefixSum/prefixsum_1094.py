import collections
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        user_at_time = [0]*1001
        for trip in trips:
            user_at_time[trip[1]] += trip[0]
            user_at_time[trip[2]] -= trip[0]

        for user_diff in user_at_time:
            capacity -= user_diff
            if capacity <0:
                return False
        return True