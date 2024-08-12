from typing import List


class Solution:

    @staticmethod
    def _canPlaceWithGap(gap: int, position: List[int], m: int) -> bool:
        prev_pos = position[0]
        remain = m - 1
        for i in range(1, len(position)):
            curr_pos = position[i]
            if curr_pos - prev_pos >= gap:
                remain -= 1
                prev_pos = curr_pos
            if remain == 0:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # position start from 1 by question description
        min_pos = 1
        max_pos = position[-1]

        low_gap = 1
        high_gap = int((max_pos - min_pos) / (m - 1.0)) + 1
        ans = 0
        while low_gap <= high_gap:
            mid = (low_gap + high_gap) // 2
            if self._canPlaceWithGap(mid, position, m):
                ans = mid
                low_gap = mid + 1
            else:
                high_gap = mid - 1
        return ans