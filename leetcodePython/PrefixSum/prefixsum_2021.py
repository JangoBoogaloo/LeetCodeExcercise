import collections
from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        bright_change = collections.defaultdict(int)
        for pos, range in lights:
            start_pos = pos - range
            end_pos = pos + range + 1
            bright_change[start_pos] += 1
            bright_change[end_pos] -= 1

        curr_bright = 0
        max_bright = float('-inf')
        ans = -1
        for pos, bright_change in sorted(bright_change.items()):
            curr_bright += bright_change
            if curr_bright > max_bright:
                max_bright = curr_bright
                ans = pos
        return ans