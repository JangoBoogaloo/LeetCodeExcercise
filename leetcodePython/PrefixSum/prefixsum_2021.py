from collections import defaultdict
from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        position_bright_change = defaultdict(int)
        for pos_i, range_i in lights:
            position_bright_change[pos_i - range_i] += 1
            position_bright_change[pos_i + range_i+1] -= 1
        max_bright = -1
        max_bright_pos = -1
        curr_bright = 0
        for pos, change in sorted(position_bright_change.items()):
            curr_bright += change
            if curr_bright > max_bright:
                max_bright = curr_bright
                max_bright_pos = pos
        return max_bright_pos
