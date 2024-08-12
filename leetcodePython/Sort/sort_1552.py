from typing import List


class Solution:

    def _canPlaceWithGap(self, gap: int, position: List[int], m: int) ->bool:
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # position start from 1 by question description
        min_pos = 1
        max_pos = position[-1]

        low_gap = 1
        high_gap = int(max_pos / (m - 1.0)) + 1
        ans = 0
        while low_gap <= high_gap:
            mid = (low_gap + high_gap) // 2
            if self._canPlaceWithGap(mid, position, m):
                ans = mid
                low_gap = mid + 1
            else:
                high_gap = mid - 1
        return ans