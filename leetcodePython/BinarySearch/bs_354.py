import bisect
from typing import List


class Solution:
    @staticmethod
    def _longestIncreaseSubseq(nums: List[int]) -> List[int]:
        sequence:List[int] = []
        for num in nums:
            idx = bisect.bisect_left(sequence, num)
            if idx == len(sequence):
                sequence.append(num)
            else:
                sequence[idx] = num
        return sequence

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        height_array = [data[1] for data in envelopes]
        return len(self._longestIncreaseSubseq(height_array))
