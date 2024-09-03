import bisect
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_index = []
        for i in range(len(s)):
            if s[i] == '|':
                candle_index.append(i)
        ans = []
        for left, right in queries:
            idx_idx_l = bisect.bisect_left(candle_index, left)
            # the actual candle index within the boundary has to be 1 index smaller
            idx_idx_r = bisect.bisect_right(candle_index, right) - 1
            plates = 0
            if idx_idx_r > idx_idx_l:
                candles_in_range = idx_idx_r - idx_idx_l
                plates = candle_index[idx_idx_r] - candle_index[idx_idx_l] - candles_in_range
            ans.append(plates)
        return ans


if __name__ == '__main__':
    sol = Solution()
    sol.platesBetweenCandles("***|**|*****|**||**|*", [[3, 6]])
