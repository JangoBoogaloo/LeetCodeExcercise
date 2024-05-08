import collections
from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        position_brightness = collections.defaultdict(int)
        for pos, range in lights:
            position_brightness[pos - range] += 1
            position_brightness[pos + range+1] -= 1

        curr_bright = 0
        max_bright = float('-inf')
        small_pos = -1
        for pos, bright in sorted(position_brightness.items()):
            curr_bright += bright
            if curr_bright > max_bright:
                max_bright = curr_bright
                small_pos = pos
        return small_pos