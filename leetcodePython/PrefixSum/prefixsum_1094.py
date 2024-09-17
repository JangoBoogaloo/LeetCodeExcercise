import collections
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # we could have 1000 position from left to right (west to east), start from index 1
        # this variable record number of passenger change at each position, by default there's no change
        passenger_change = [0] * 1001
        for passenger, start, end in trips:
            passenger_change[start] += passenger
            passenger_change[end] -= passenger

        for change in passenger_change:
            capacity -= change
            if capacity < 0:
                return False
        return True
